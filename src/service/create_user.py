import requests
from src.config import URL_REQRES
from src.service.file_reader import file_reader
from src.service.generate_schema.generate_json_from_schema import generate_user_data_json
import logging


def create_user():
    loaded_schema = file_reader(filename='../service/generate_schema/create_user_schema.json')
    logger = logging.getLogger(__name__)
    VALID_BODY = generate_user_data_json(loaded_schema)

    try:
        response = requests.post(f"{URL_REQRES}/register", json=VALID_BODY)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()["id"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error creating user: {e}")
        return None  # Handle the error appropriately, e.g., return a special value or raise an exception
