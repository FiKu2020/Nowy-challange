# pip instal cryptography
from cryptography.hazmat.primitives import hashes
# ^ https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/#elliptic-curves
from cryptography.hazmat.primitives.asymmetric import ec
# ^ https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/
# w komentarzach masz dokumentacje :)

def generate_key():
    our_public_key = our_private_key.public_key()
    our_private_key = "temp"
    return(our_public_key,our_private_key)

def encrypt_message(message, public_key):
    ciphered_text = public_key.encrypt(message.encode())
    return ciphered_text

def decrypt_message(private_key, ciphered_text):
    czytelny = private_key.decrypt(ciphered_text,)

    