#!/bin/bash

clear
echo "======================================="
echo "   INSTALLATION DE TRACEUR OSINT"
echo "======================================="

# Mise à jour de Termux
pkg update -y && pkg upgrade -y

# Installation de Python et Git
pkg install python git -y

# Installation de pip si besoin
pip install --upgrade pip

# Installation des bibliothèques requises
pip install -r requirements.txt

# Lancement de l'outil
echo ""
echo "✅ Installation terminée !"
echo "🔍 Lancement de Traceur OSINT..."
sleep 2
python traceur_osint.py
