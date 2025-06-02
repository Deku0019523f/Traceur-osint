#!/bin/bash

clear
echo -e "\033[1;92m📦 Mise à jour des paquets Termux...\033[0m"
pkg update -y && pkg upgrade -y

echo -e "\n\033[1;92m📦 Installation de Python et Git...\033[0m"
pkg install -y python git

echo -e "\n\033[1;92m📦 Installation de pip et modules nécessaires...\033[0m"
pip install requests phonenumbers

echo -e "\n\033[1;92m📁 Configuration de Traceur-OSINT...\033[0m"

# Vérifie si le dossier est déjà là
if [ ! -d "$HOME/Traceur-osint" ]; then
    git clone https://github.com/Deku0019523f/Traceur-osint.git $HOME/Traceur-osint
else
    echo "📂 Le dossier Traceur-osint existe déjà."
fi

# Ajout d'un alias au .bashrc ou .zshrc
echo -e "\n\033[1;92m🔧 Création du raccourci 'traceur'...\033[0m"
if [ -f "$HOME/.bashrc" ]; then
    echo 'alias traceur="python $HOME/Traceur-osint/traceur_osint.py"' >> $HOME/.bashrc
elif [ -f "$HOME/.zshrc" ]; then
    echo 'alias traceur="python $HOME/Traceur-osint/traceur_osint.py"' >> $HOME/.zshrc
fi

# Rendre le script exécutable
chmod +x $HOME/Traceur-osint/traceur_osint.py

echo -e "\n\033[1;96m🚀 Lancement de Traceur...\033[0m"
python $HOME/Traceur-osint/traceur_osint.py

echo -e "\n\033[1;93m👋 Merci d'avoir utilisé DEKU225 Traceur-OSINT. À la prochaine !\033[0m"
