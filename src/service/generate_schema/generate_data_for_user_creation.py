import string
import secrets

def generate_password(length=4):
    """
    Generate a random password.

    Parameters:
    - length: The length of the password (default is 12).

    Returns:
    A generated password string.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password



