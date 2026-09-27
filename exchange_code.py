import json
import requests
from pathlib import Path


PROJECT_DIR = Path(__file__).parent

SECRETS_FILE = PROJECT_DIR / "secrets.json"
TOKENS_FILE = PROJECT_DIR / "tokens.json"


REDIRECT_URI = (
    "https://julco3.github.io/fleet-test/callback"
)

TOKEN_URL = (
    "https://fleet-auth.prd.vn.cloud.tesla.com"
    "/oauth2/v3/token"
)

AUDIENCE = (
    "https://fleet-api.prd.eu.vn.cloud.tesla.com"
)


def load_secrets():

    with SECRETS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def exchange_code(code):

    secrets = load_secrets()

    data = {
        "grant_type": "authorization_code",
        "client_id": secrets["client_id"],
        "client_secret": secrets["client_secret"],
        "code": code,
        "audience": "https://fleet-api.prd.eu.vn.cloud.tesla.com",
        "redirect_uri": "https://julco3.github.io/fleet-test/callback"
    }

    response = requests.post(
        TOKEN_URL,
        data=data,
        timeout=30,
    )

    print()
    print("Réponse Tesla :")
    print(response.status_code)
    print(response.text)
    print()

    response.raise_for_status()

    return response.json()


def main():

    code = input("Colle ici le code Tesla : ").strip()

    token_data = exchange_code(code)

    with TOKENS_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            token_data,
            file,
            indent=4,
        )

    print()
    print("Authentification réussie.")
    print()
    print("Tokens enregistrés dans :")
    print(TOKENS_FILE)


if __name__ == "__main__":
    main()