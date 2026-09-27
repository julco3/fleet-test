from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from pathlib import Path


PROJECT_DIR = Path(__file__).parent

PRIVATE_KEY_FILE = PROJECT_DIR / "private-key.pem"
PUBLIC_KEY_FILE = PROJECT_DIR / "public-key.pem"


# Génération de la clé privée P-256
private_key = ec.generate_private_key(
    ec.SECP256R1()
)


# Sauvegarde de la clé privée
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

PRIVATE_KEY_FILE.write_bytes(private_bytes)


# Récupération de la clé publique
public_key = private_key.public_key()

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

PUBLIC_KEY_FILE.write_bytes(public_bytes)


print("Clés générées :")
print(PRIVATE_KEY_FILE)
print(PUBLIC_KEY_FILE)