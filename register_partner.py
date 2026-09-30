import json
import requests
from pathlib import Path


PROJECT_DIR = Path(__file__).parent

PARTNER_TOKEN_FILE = PROJECT_DIR / "partner_token.json"

BASE_URL = "https://fleet-api.prd.eu.vn.cloud.tesla.com"

DOMAIN = "julco3.github.io"


def load_partner_token():
    with PARTNER_TOKEN_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def register_partner():
    token_data = load_partner_token()

    headers = {
        "Authorization": "Bearer " + token_data["access_token"],
        "Content-Type": "application/json",
    }

    data = {
        "domain": DOMAIN,
    }

    response = requests.post(
        BASE_URL + "/api/1/partner_accounts",
        headers=headers,
        json=data,
        timeout=30,
    )

    print("Status :", response.status_code)
    print("Réponse Tesla :")
    print(response.text)
    print()

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    register_partner()