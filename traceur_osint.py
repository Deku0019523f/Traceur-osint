import os
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialisation de colorama
init(autoreset=True)

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(Fore.MAGENTA + "¥" * 60)
    fig = Figlet(font="block")  # Autres options: 'slant', 'standard', 'big'
    print(Fore.RED + fig.renderText("DEKU225"))
    print(Fore.MAGENTA + "¥" * 60 + "\n")
    print(Fore.GREEN + "[1] L'ADRESSE IP")
    print("[2] NUMÉRO TÉLÉPHONE\n")
    print(Fore.YELLOW + "CHOOSE AN OPTION : ", end="")

def trace_ip():
    ip = input(Fore.CYAN + "\n🔎 Entrez une adresse IP : ")
    print(Fore.YELLOW + f"📡 Recherche simulée d'infos sur l'IP : {ip}")
    # Simulation d'infos — à remplacer par une vraie API si souhaité
    print(Fore.GREEN + f"\nIP : {ip}\nLocalisation : Côte d'Ivoire\nFournisseur : MTN\n...")

def trace_phone():
    import phonenumbers
    from phonenumbers import geocoder, carrier

    number = input(Fore.CYAN + "\n📞 Entrez un numéro avec indicatif (ex: +2250700000000) : ")
    parsed = phonenumbers.parse(number)

    country = geocoder.description_for_number(parsed, "fr")
    operator = carrier.name_for_number(parsed, "fr")

    print(Fore.GREEN + f"\n📍 Pays : {country}")
    print(f"📶 Opérateur : {operator}")

if __name__ == "__main__":
    banner()
    choice = input()
    if choice == "1":
        trace_ip()
    elif choice == "2":
        trace_phone()
    else:
        print(Fore.RED + "❌ Option invalide.")
