"""
This module used the cryptography and contain a encryption and decryption 
- fernet encrypt
- fernet decrypt
"""

from cryptography.fernet import Fernet

fernet_secrete_key = "3RWyplGjRJIyeiteD1A7-HFKKk0ehVXzU8ZUfB19hMs="
fernet = Fernet(fernet_secrete_key)

def fernet_encrypt(data = None):
    """
    This encrypt parsed message using fernet with secrete key 
    """
    try:
        if not data:
            return None
        return fernet.encrypt(data.encode())
    except:
        return None

def fernet_decrypt(data = None):
    """
    Decrypt the message using the above secrete key
    """
    try:
        if not data:
            return None
        return fernet.decrypt(data).decode()
    except:
        return None