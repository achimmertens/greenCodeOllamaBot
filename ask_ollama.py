#!/usr/bin/env python3

import requests
import json
import logging

# Konfiguration des Loggings
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Datei-Handler
file_handler = logging.FileHandler('ask_ollama.log')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Konsolen-Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

def frage_ollama(frage):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "greenCodeLlama318b",
        "prompt": frage,
        "stream": False
    }

    logging.info(f"Frage an Ollama: {frage}")

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        antwort = response.json()
        logging.info(f"Antwort von Ollama: {antwort['response']}")
        return antwort['response']
    except requests.RequestException as e:
        logging.error(f"Fehler bei der Anfrage: {e}")
        return f"Fehler bei der Anfrage: {e}"

def lese_frage_aus_datei(dateipfad):
    try:
        with open(dateipfad, 'r') as datei:
            frage = datei.read().strip()
            logging.info(f"Frage aus Datei gelesen: {frage}")
            return frage
    except FileNotFoundError:
        logging.error(f"Datei nicht gefunden: {dateipfad}")
        return None
    except Exception as e:
        logging.error(f"Fehler beim Lesen der Datei: {e}")
        return None

if __name__ == "__main__":
    dateipfad = 'frage.txt'
    frage = lese_frage_aus_datei(dateipfad)

    if frage:
        antwort = frage_ollama(frage)
        print(f"Frage: {frage}")
        print(f"Antwort: {antwort}")
    else:
        print("Fehler beim Lesen der Frage aus der Datei. Siehe Protokoll für Details.")
