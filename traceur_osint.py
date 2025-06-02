
import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def trace_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        data = response.json()
        print("\n📍 Résultat IP :")
        print(f"  IP : {data['query']}")
        print(f"  Pays : {data['country']} - Ville : {data['city']}")
        print(f"  Région : {data['regionName']}")
        print(f"  Latitude / Longitude : {data['lat']} / {data['lon']}")
        print(f"  FAI : {data['isp']}")
    except:
        print("❌ Impossible de tracer cette IP.")

def trace_number(phone):
    try:
        num = phonenumbers.parse(phone)
        localisation = geocoder.description_for_number(num, "fr")
        operateur = carrier.name_for_number(num, "fr")
        print("\n📞 Résultat Numéro :")
        print(f"  Numéro : {phone}")
        print(f"  Localisation : {localisation}")
        print(f"  Opérateur : {operateur}")
    except:
        print("❌ Numéro invalide ou erreur de traitement.")

def osint_google_search(query):
    print("\n🔎 Recherches Google possibles :")
    print(f"  🔗 https://www.google.com/search?q={query}")
    print(f"  🔗 https://www.google.com/search?q=\"{query}\"+site:facebook.com")
    print(f"  🔗 https://www.google.com/search?q=\"{query}\"+site:instagram.com")
    print(f"  🔗 https://www.google.com/search?q=\"{query}\"+site:linkedin.com")

if __name__ == "__main__":
    print("🔍 Outil OSINT légal - IP, numéro, recherches\n")

    ip = input("Entrez une adresse IP (ou appuyez sur Entrée pour ignorer) : ")
    if ip:
        trace_ip(ip)

    phone = input("\nEntrez un numéro de téléphone (ex: +33612345678) : ")
    if phone:
        trace_number(phone)

    recherche = input("\nEntrez un nom, email, numéro ou pseudo à chercher (ou vide pour ignorer) : ")
    if recherche:
        osint_google_search(recherche)

    print("\n✅ Fini. Utilisation légale uniquement, respect de la vie privée obligatoire.")
