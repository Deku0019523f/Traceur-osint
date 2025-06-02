
import tkinter as tk
from tkinter import messagebox
import requests
import phonenumbers
from phonenumbers import geocoder, carrier
import webbrowser

def trace_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        result = f"📍 Résultat IP :\n"
        result += f"IP : {data['query']}\n"
        result += f"Pays : {data['country']} - Ville : {data['city']}\n"
        result += f"Région : {data['regionName']}\n"
        result += f"Latitude / Longitude : {data['lat']} / {data['lon']}\n"
        result += f"FAI : {data['isp']}\n"
        return result
    except:
        return "❌ Impossible de tracer cette IP."

def trace_number(phone):
    try:
        num = phonenumbers.parse(phone)
        localisation = geocoder.description_for_number(num, "fr")
        operateur = carrier.name_for_number(num, "fr")
        result = f"📞 Résultat Numéro :\n"
        result += f"Numéro : {phone}\n"
        result += f"Localisation : {localisation}\n"
        result += f"Opérateur : {operateur}\n"
        return result
    except:
        return "❌ Numéro invalide ou erreur de traitement."

def osint_search_links(query):
    links = [
        f"https://www.google.com/search?q={query}",
        f"https://www.google.com/search?q=\"{query}\"+site:facebook.com",
        f"https://www.google.com/search?q=\"{query}\"+site:instagram.com",
        f"https://www.google.com/search?q=\"{query}\"+site:linkedin.com",
    ]
    return links

def run_trace():
    result_text.delete(1.0, tk.END)
    if ip_entry.get():
        result_text.insert(tk.END, trace_ip(ip_entry.get()) + "\n\n")
    if phone_entry.get():
        result_text.insert(tk.END, trace_number(phone_entry.get()) + "\n\n")
    if search_entry.get():
        result_text.insert(tk.END, "🔎 Recherches OSINT :\n")
        for link in osint_search_links(search_entry.get()):
            result_text.insert(tk.END, link + "\n")

# Interface graphique
app = tk.Tk()
app.title("Traceur OSINT")
app.geometry("600x500")

tk.Label(app, text="Adresse IP :").pack()
ip_entry = tk.Entry(app, width=60)
ip_entry.pack()

tk.Label(app, text="Numéro de téléphone (+33...) :").pack()
phone_entry = tk.Entry(app, width=60)
phone_entry.pack()

tk.Label(app, text="Nom, pseudo ou email à chercher :").pack()
search_entry = tk.Entry(app, width=60)
search_entry.pack()

tk.Button(app, text="Lancer la recherche", command=run_trace).pack(pady=10)

result_text = tk.Text(app, wrap=tk.WORD, height=20)
result_text.pack(expand=True, fill='both')

app.mainloop()
