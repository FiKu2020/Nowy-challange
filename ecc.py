# pip instal cryptography
from cryptography.hazmat.primitives import hashes
# ^ https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/#elliptic-curves
from cryptography.hazmat.primitives.asymmetric import ec
# ^ https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/
# w komentarzach masz dokumentacje :)

def generate_key():
    public_key = "temp"
    private_key = "temp"

def encrypt_message(message, public_key):
    pass

def decrypt_message(private_key, ciphered_text):
    pass