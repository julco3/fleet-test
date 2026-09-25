from urllib.parse import urlencode
import secrets
import webbrowser


CLIENT_ID = "92ff08f2-1227-480e-9d6d-941d49115eb5"

REDIRECT_URI = (
    "https://julco3.github.io/fleet-test/callback"
)

SCOPES = [
    "openid",
    "offline_access",
    "vehicle_device_data",
]


def create_authorization_url():
    state = secrets.token_urlsafe(32)

    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": " ".join(SCOPES),
        "state": state,
    }

    url = (
        "https://auth.tesla.com/oauth2/v3/authorize?"
        + urlencode(params)
    )

    return url, state


if __name__ == "__main__":

    url, state = create_authorization_url()

    print("URL d'authentification Tesla :")
    print()
    print(url)
    print()
    print("State :")
    print(state)
    print()

    webbrowser.open(url)