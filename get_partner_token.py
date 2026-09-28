import json
import requests
from pathlib import Path


PROJECT_DIR = Path(__file__).parent

SECRETS_FILE = PROJECT_DIR / "secrets.json"
PARTNER_TOKEN_FILE = PROJECT_DIR / "partner_token.json"

TOKEN_URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"

AUDIENCE = "https://fleet-api.prd.eu.vn.cloud.tesla.com"


def load_secrets():
    with SECRETS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_partner_token():
    secrets = load_secrets()

    data = {
        "grant_type": "client_credentials",
        "client_id": secrets["client_id"],
        "client_secret": secrets["client_secret"],
        "audience": AUDIENCE,
    }

    response = requests.post(
        TOKEN_URL,
        data=data,
        timeout=30,
    )

    print("Status :", response.status_code)
    print("Réponse :", response.text)

    response.raise_for_status()

    return response.json()


def main():
    token_data = get_partner_token()

    with PARTNER_TOKEN_FILE.open("w", encoding="utf-8") as file:
        json.dump(token_data, file, indent=4)

    print()
    print("Partner Token obtenu.")
    print("Enregistré dans :", PARTNER_TOKEN_FILE)


if __name__ == "__main__":
    main()
