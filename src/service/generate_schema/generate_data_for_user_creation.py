import string
import secrets
import random


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


def generate_random_user():
    # Sample data for names and job roles
    names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"]
    job_roles = ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer", "Marketing Specialist",
                 "Sales Representative"]

    # Generate a random name and job role
    random_name = random.choice(names)
    random_job_role = random.choice(job_roles)

    return random_name, random_job_role


