import json
import requests
from pathlib import Path


PROJECT_DIR = Path(__file__).parent
TOKENS_FILE = PROJECT_DIR / "tokens.json"

BASE_URL = (
    "https://fleet-api.prd.eu.vn.cloud.tesla.com"
)


def load_tokens():

    with TOKENS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_vehicles():

    tokens = load_tokens()

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    response = requests.get(
        BASE_URL + "/api/1/vehicles",
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    data = get_vehicles()

    print(json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    ))