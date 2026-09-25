from pathlib import Path
import json
from datetime import datetime


# --------------------------------------------------
# Configuration
# --------------------------------------------------

PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data"

RAW_FILE = DATA_DIR / "raw.json"
CURRENT_FILE = DATA_DIR / "current.json"
HISTORY_FILE = DATA_DIR / "history.json"


# --------------------------------------------------
# Données fictives
# --------------------------------------------------

def get_fake_tesla_data():
    """Simule la réponse brute de l'API Tesla."""

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),

        "vehicle": {
            "model": "Model Y Long Range",
            "vin": "TEST"
        },

        "battery": {
            "level": 72,
            "range_km": 418
        },

        "vehicle_state": {
            "odometer_km": 12543,
            "locked": True,
            "charging_state": "Disconnected"
        },

        "temperature": {
            "outside_c": 14.0,
            "inside_c": 21.5
        }
    }


# --------------------------------------------------
# Sauvegarde JSON
# --------------------------------------------------

def save_json(data, filename):
    """Sauvegarde un dictionnaire dans un fichier JSON."""

    DATA_DIR.mkdir(exist_ok=True)

    with filename.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# --------------------------------------------------
# Historique
# --------------------------------------------------

def save_history(data):
    """Ajoute une mesure à l'historique."""

    DATA_DIR.mkdir(exist_ok=True)

    if HISTORY_FILE.exists():

        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            history = json.load(file)

    else:
        history = []

    history.append(data)

    save_json(history, HISTORY_FILE)


# --------------------------------------------------
# Programme principal
# --------------------------------------------------

def main():

    print("Récupération des données Tesla...")

    # Pour le moment : données fictives
    raw_data = get_fake_tesla_data()

    # 1. Réponse brute
    save_json(raw_data, RAW_FILE)

    # 2. Pour le moment, current = données brutes
    save_json(raw_data, CURRENT_FILE)

    # 3. Ajout à l'historique
    save_history(raw_data)

    print()
    print("Données enregistrées :")
    print(f"  Raw     : {RAW_FILE}")
    print(f"  Current : {CURRENT_FILE}")
    print(f"  History : {HISTORY_FILE}")


if __name__ == "__main__":
    main()