import requests
from src.config import URL_REQRES
from src.service.create_user import create_user


def list_user(user_id):
    # Create and get user id
    USER_ID = create_user()
    user_id = USER_ID
    response = requests.get(f'{URL_REQRES}/users/{user_id}')
    return response.json()["data"], USER_ID
