import requests
from requests.adapters import HTTPAdapter, Retry

SESSION = requests.Session()
retries = Retry(total=3, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504))
SESSION.mount("https://", HTTPAdapter(max_retries=retries))

def trace_ip(ip):
    try:
        url = f"https://ip-api.com/json/{ip}?fields=status,message,query,country,regionName,city,lat,lon,isp"
        resp = SESSION.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != "success":
            return f"❌ Échec IP: {data.get('message','inconnu')}"
        return (
            "📍 Résultat IP :\n"
            f"IP : {data.get('query','?')}\n"
            f"Pays : {data.get('country','?')} - Ville : {data.get('city','?')}\n"
            f"Région : {data.get('regionName','?')}\n"
            f"Latitude / Longitude : {data.get('lat','?')} / {data.get('lon','?')}\n"
            f"FAI : {data.get('isp','?')}\n"
        )
    except requests.Timeout:
        return "⏳ Délai dépassé."
    except requests.RequestException as e:
        return f"❌ Erreur réseau : {e}"
