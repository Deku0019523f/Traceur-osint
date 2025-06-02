
import os
import time
import requests
import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers.phonenumberutil import number_type
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(Fore.RED + "¥" * 50)
    print(Fore.RED + " " * 10 + "DEKU225".center(30))
    print(Fore.RED + "¥" * 50 + "\n")

def trace_ip():
    ip = input(Fore.CYAN + "\nEntrez une adresse IP : ")
    print(Fore.YELLOW + "[~] Recherche en cours...\n")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "success":
            print(Fore.GREEN + f"Pays: {response['country']}")
            print(Fore.GREEN + f"Région: {response['regionName']}")
            print(Fore.GREEN + f"Ville: {response['city']}")
            print(Fore.GREEN + f"Fournisseur: {response['isp']}")
            print(Fore.GREEN + f"Adresse IP: {response['query']}")
        else:
            print(Fore.RED + "[!] IP invalide ou introuvable.")
    except Exception as e:
        print(Fore.RED + f"[!] Erreur: {e}")

def trace_num():
    num = input(Fore.CYAN + "\nEntrez le numéro de téléphone (avec l'indicatif +33, +225, etc.) : ")
    try:
        phone = phonenumbers.parse(num)
        if not phonenumbers.is_valid_number(phone):
            print(Fore.RED + "[!] Numéro invalide.")
            return
        print(Fore.GREEN + f"Pays: {geocoder.description_for_number(phone, 'fr')}")
        print(Fore.GREEN + f"Opérateur: {carrier.name_for_number(phone, 'fr')}")
        print(Fore.GREEN + f"Type: {number_type(phone)}")
    except Exception as e:
        print(Fore.RED + f"[!] Erreur: {e}")

def main():
    banner()
    print(Fore.YELLOW + "[1] L'ADRESSE IP")
    print(Fore.YELLOW + "[2] NUMÉRO TÉLÉPHONE")
    print(Fore.YELLOW + "[0] QUITTER\n")
    choix = input(Fore.CYAN + "CHOISIS UNE OPTION : ")

    if choix == "1":
        trace_ip()
    elif choix == "2":
        trace_num()
    elif choix == "0":
        print(Fore.GREEN + "\nAu revoir !")
        return
    else:
        print(Fore.RED + "\n[!] Option invalide.")

    input(Fore.MAGENTA + "\nAppuie sur Entrée pour continuer...")
    main()

if __name__ == "__main__":
    main()
    
