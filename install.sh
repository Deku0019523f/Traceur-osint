
#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\033[1;31m"
echo "========================================="
echo "       INSTALLATION DEKU225 TRACEUR      "
echo "========================================="
echo -e "\033[0m"

echo "[1/6] 📦 Installation de Python et Git..."
pkg install -y python git

echo "[2/6] 📦 Installation de pip et dépendances..."
pip install --upgrade pip
pip install requests phonenumbers colorama

echo "[3/6] 🔁 Clonage du dépôt..."
git clone https://github.com/Deku0019523f/Traceur-osint.git
cd Traceur-osint

echo "[4/6] 🛠️  Installation via requirements.txt..."
pip install -r requirements.txt

echo "[5/6] ✅ Configuration terminée !"
echo "[6/6] 🚀 Lancement de l'outil..."

sleep 2
python traceur_osint.py
