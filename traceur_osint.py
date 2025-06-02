import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def afficher_banniere():
    print("¥" * 50)
    print("\033[1;91m")
    print(r"""██████╗ ███████╗██╗  ██╗██╗   ██╗██╗  ██╗███████╗███████╗
██╔══██╗██╔════╝██║ ██╔╝╚██╗ ██╔╝██║ ██╔╝██╔════╝██╔════╝
██████╔╝█████╗  █████╔╝  ╚████╔╝ █████╔╝ █████╗  ███████╗
██╔═══╝ ██╔══╝  ██╔═██╗   ╚██╔╝  ██╔═██╗ ██╔══╝  ╚════██║
██║     ███████╗██║  ██╗   ██║   ██║  ██╗███████╗███████║
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝""")
    print("\033[0m")
    print("¥" * 50)

def tracer_ip(ip):
    print(f"\n🔍 Recherche d'informations sur l'adresse IP : {ip}")
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        for k, v in data.items():
            print(f"{k.upper():<15} ➤ {v}")
    except Exception as e:
        print(f"Erreur lors de la requête : {e}")

def tracer_numero(numero):
    print(f"\n📞 Analyse du numéro : {numero}")
    try:
        parsed = phonenumbers.parse(numero)
        pays = geocoder.description_for_number(parsed, "fr")
        operateur = carrier.name_for_number(parsed, "fr")
        print(f"Pays         ➤ {pays}")
        print(f"Opérateur    ➤ {operateur}")
        print(f"Valide       ➤ {phonenumbers.is_valid_number(parsed)}")
    except Exception as e:
        print(f"Erreur : {e}")

def menu():
    afficher_banniere()
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
        print("À bientôt ! 👋")
        exit()
    else:
        print("❌ Option invalide")

if __name__ == "__main__":
    while True:
        menu()
        input("\nAppuie sur Entrée pour revenir au menu...")
