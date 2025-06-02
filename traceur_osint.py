import requests
import phonenumbers
from phonenumbers import geocoder, carrier
import sys

def afficher_titre():
    print("\n" + "¥" * 60)
    print(" " * 20 + "\033[91mDEKU225\033[0m")
    print("¥" * 60 + "\n")

def tracer_ip(ip):
    print(f"\n🔍 Recherche d'informations sur l'adresse IP : \033[92m{ip}\033[0m")
    url = f"https://ipinfo.io/{ip}/json"
    headers = {"User-Agent": "Traceur-OSINT by DEKU225"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        for k, v in data.items():
            print(f"{k.upper():<15} ➤ {v}")
    except requests.exceptions.Timeout:
        print("⏳ Délai dépassé. Vérifie ta connexion.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la requête : {e}")

def tracer_numero(numero):
    print(f"\n📞 Analyse du numéro : \033[92m{numero}\033[0m")
    try:
        parsed = phonenumbers.parse(numero)
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

def menu():
    afficher_titre()
    print("\033[93m[1] L'ADRESSE IP")
    print("[2] NUMÉRO TÉLÉPHONE")
    print("[0] QUITTER\033[0m")
    
    choix = input("\n\033[96mCHOISIS UNE OPTION : \033[0m")

    if choix == "1":
        ip = input("Entre une adresse IP : ")
        tracer_ip(ip)
    elif choix == "2":
        numero = input("Entre le numéro de téléphone (ex: +225...) : ")
        tracer_numero(numero)
    elif choix == "0":
        print("\n🟥 Merci d'avoir utilisé \033[91mDEKU225 - TRACEUR OSINT\033[0m. À bientôt 👋")
        sys.exit()
    else:
        print("\n❌ Option invalide.")

if __name__ == "__main__":
    while True:
        menu()
        input("\n⏎ Appuie sur Entrée pour revenir au menu...")
