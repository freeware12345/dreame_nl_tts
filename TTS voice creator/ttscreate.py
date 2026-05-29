import csv
import os
import subprocess
import sys

# CSV bestand instellen op jouw Nederlandse bestand
csv_path = "all_dreame_nl.csv"

# Nederlandse stemopties instellen (Fenna of Maarten)
voice_options = ["Fenna", "Maarten"]
voice = sys.argv[1] if len(sys.argv) > 1 else input(f"Kies een stem ({'/'.join(voice_options)}): ").capitalize()

# Automatische conversie aanroepen na het downloaden
run_conversion = 'igen' if len(sys.argv) > 2 and sys.argv[2] == '--convert' else input("Conversie uitvoeren na het downloaden? (igen/nem): ")

# Controleer of het CSV-bestand bestaat
if not os.path.exists(csv_path):
    print(f"Bestand niet gevonden: {csv_path}")
    sys.exit()

# Controleer of de gekozen stem geldig is
if voice not in voice_options:
    voice = input(f"Kies een stem ({'/'.join(voice_options)}): ").capitalize()

# CSV bestand inlezen en regel voor regel verwerken
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    for row in csvreader:
        print(f"{row['Text']}", end='')
        # Start het PHP-script op de achtergrond met de Nederlandse tekst en stem
        php_command = f'php bing_hu_voice.php "{row["Text"]}" "{row["Code"]}" {voice}'
        subprocess.run(php_command, shell=True)
        print(" ... done!")

# Start de conversie naar OGG-formaat via convert.py
if run_conversion.lower() == 'igen':
    py_command = f"python convert.py {voice}"
    subprocess.run(py_command, shell=True)
