
<p align="center">
  <img src="https://raw.githubusercontent.com/Deku0019523f/Traceur-osint/main/logo.png" width="150" alt="Logo OSINT">
</p>


# 🔍 Traceur OSINT - IP, Téléphone, Réseaux (avec interface graphique)

Un outil Python simple pour tracer **une adresse IP**, obtenir des infos sur **un numéro de téléphone**, et générer des **liens de recherche OSINT** sur les réseaux sociaux et Google.

---

## 🖥️ Fonctionnalités

- 📍 Localisation approximative d'une adresse IP (pays, ville, FAI)
- 📞 Informations sur un numéro de téléphone (opérateur, localisation)
- 🔎 Liens OSINT pour recherche sur Google, Facebook, Instagram, LinkedIn
- 🖼️ Interface graphique simple avec Tkinter

---

## 📦 Installation (Ordinateur Linux / Windows / Termux)

### 🐧 Sous Linux ou Termux (Android)

```bash
pkg update && pkg upgrade
pkg install python
pip install requests phonenumbers tk
```

### 🪟 Sous Windows

1. Installe Python depuis [https://www.python.org](https://www.python.org)
2. Dans un terminal :

```bash
pip install requests phonenumbers
```

> Tkinter est généralement préinstallé avec Python sur Windows et Linux.

---

## 🚀 Lancement

### Interface Graphique

```bash
python traceur_osint_gui.py
```

### En ligne de commande (si tu veux la version terminal)

```bash
python traceur_osint.py
```

---

## 📝 Exemple de résultat

- IP : 8.8.8.8  
  → Pays : USA, Ville : Mountain View  
- Téléphone : +33612345678  
  → Localisation : France, Opérateur : Orange  
- Nom/pseudo : `johnsmith`  
  → Liens de recherche vers Google, Facebook, Instagram...

---

## ⚠️ Avertissement Légal

Cet outil est **strictement éducatif et légal**.  
Il **n’effectue aucune géolocalisation réelle**, ni suivi GPS, ni accès aux données personnelles privées.  
Toute utilisation abusive ou illégale est sous votre propre responsabilité.

---

## 👤 Auteur

Développé par [Deku225]  
Licence : MIT

---

## 🌐 Liens utiles

- [IP-API.com](http://ip-api.com) (localisation IP)
- [Phonenumbers](https://pypi.org/project/phonenumbers/) (numéros de téléphone)
- [Google Dork OSINT](https://www.exploit-db.com/google-hacking-database)
ing-database)
