# --- top of file ---
import argparse
import ipaddress
import requests
from requests.adapters import HTTPAdapter, Retry
import phonenumbers
from phonenumbers import geocoder, carrier
import sys

SESSION = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504))
SESSION.mount("https://", HTTPAdapter(max_retries=retries))

def is_valid_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def tracer_ip(ip: str):
    if not is_valid_ip(ip):
        print("⚠️ IP invalide.")
        return
    print(f"\n🔍 Recherche d'informations sur l'adresse IP : \033[92m{ip}\033[0m")
    url = f"https://ip-api.com/json/{ip}?fields=status,message,query,country,regionName,city,lat,lon,isp"
    headers = {"User-Agent": "Traceur-OSINT"}
    try:
        resp = SESSION.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != "success":
            print(f"❌ Échec: {data.get('message','inconnu')}")
            return
        fields = {
            "IP": data.get("query"),
            "Pays": data.get("country"),
            "Région": data.get("regionName"),
            "Ville": data.get("city"),
            "Latitude": data.get("lat"),
            "Longitude": data.get("lon"),
            "FAI": data.get("isp"),
        }
        for k, v in fields.items():
            print(f"{k:<12} ➤ {v}")
    except requests.exceptions.Timeout:
        print("⏳ Délai dépassé. Vérifie ta connexion.")
    except requests.RequestException as e:
        print(f"❌ Erreur lors de la requête : {e}")

def tracer_numero(numero: str, region_default: str = "FR"):
    print(f"\n📞 Analyse du numéro : \033[92m{numero}\033[0m")
    try:
        parsed = phonenumbers.parse(numero, region_default)
        if not phonenumbers.is_valid_number(parsed):
            print("❌ Numéro invalide.")
            return
        pays = geocoder.description_for_number(parsed, "fr")
        operateur = carrier.name_for_number(parsed, "fr")
        valide = phonenumbers.is_valid_number(parsed)
        print(f"Pays         ➤ {pays}")
        print(f"Opérateur    ➤ {operateur}")
        print(f"Valide       ➤ {valide}")
    except phonenumbers.NumberParseException:
        print("⚠️ Format de numéro incorrect.")
    except Exception as e:
        print(f"❌ Erreur : {e}")

def main():
    parser = argparse.ArgumentParser(prog="traceur-osint", description="Trace IP, numéros et liens OSINT")
    parser.add_argument("--ip", help="Adresse IP à analyser")
    parser.add_argument("--phone", help="Numéro de téléphone (ex: +225..., 0612..., etc.)")
    parser.add_argument("--region", default="FR", help="Région par défaut pour parser les numéros (FR, US, ...)")
    parser.add_argument("--interactive", action="store_true", help="Lancer le menu interactif")
    args = parser.parse_args()

    ran = False
    if args.ip:
        tracer_ip(args.ip); ran = True
    if args.phone:
        tracer_numero(args.phone, args.region); ran = True

    if args.interactive or not ran:
        # ton menu existant peut rester inchangé, sinon on peut offrir un simple loop
        while True:
            print("\n[1] Adresse IP\n[2] Numéro téléphone\n[0] Quitter")
            choix = input("Choisis une option: ").strip()
            if choix == "1":
                ip = input("Entre une adresse IP : ")
                tracer_ip(ip)
            elif choix == "2":
                numero = input("Entre le numéro (ex: +225...) : ")
                tracer_numero(numero, args.region)
            elif choix == "0":
                print("\n🟥 Merci d'avoir utilisé TRACEUR OSINT. À bientôt 👋")
                sys.exit(0)
            else:
                print("❌ Option invalide.")

if __name__ == "__main__":
    main()
