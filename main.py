from pathlib import Path
import json
from datetime import datetime


# Dossier du projet
PROJECT_DIR = Path(__file__).parent

# Fichier de données
DATA_FILE = PROJECT_DIR / "data" / "tesla.json"


def get_fake_tesla_data():
    """Retourne des données fictives pour tester le fonctionnement."""

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


def save_data(data):
    """Enregistre les données dans le fichier JSON."""

    DATA_FILE.parent.mkdir(exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():

    print("Récupération des données Tesla...")

    data = get_fake_tesla_data()

    save_data(data)

    print(f"Données enregistrées dans : {DATA_FILE}")


if __name__ == "__main__":
    main()