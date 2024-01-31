import requests
from src.config import URL_REQRES
from src.service.file_reader import file_reader
from src.service.generate_schema.generate_json_from_schema import generate_user_data_json


import logging

class TestCreateUser:

    @classmethod
    def setup_class(cls):
        cls.loaded_schema = file_reader(filename='../service/generate_schema/create_user_schema.json')
        cls.URL_REQRES = f"{URL_REQRES}/register"
        cls.logger = logging.getLogger(__name__)

    def test_should_create_a_new_user_DCL_T2285(self):
        """Should create a new user when pass valid parameters"""

        VALID_BODY = generate_user_data_json(self.loaded_schema)

        try:
            response = requests.post(self.URL_REQRES, json=VALID_BODY)
            response.raise_for_status()

            assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"
            assert "id" in response.json() and type(response.json()["id"] == int), "Response should contain 'id' field and must be an integer"
            assert "token" in response.json() and type(response.json()["token"] == str), "Response should contain 'token' field and must be a string"

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating user: {e}")
            assert False


