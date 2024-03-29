import requests
from src.config import URL_REQRES
from src.service.file_reader import file_reader
from src.service.generate_schema.generate_json_from_schema import generate_user_data_json
import logging
from src.service.modify_schema import modify_json_values


class TestCreateUser:

    def setup_class(self):
        self.loaded_schema = file_reader(filename='../service/generate_schema/create_user_schema.json')
        self.URL_REQRES = f"{URL_REQRES}/register"
        self.logger = logging.getLogger(__name__)

    def test_should_create_a_new_user(self):
        """Should create a new user when pass valid parameters"""

        VALID_BODY = generate_user_data_json(self.loaded_schema)

        try:
            response = requests.post(self.URL_REQRES, json=VALID_BODY)
            assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"
            assert "id" in response.json() and type(
                response.json()["id"] == int), "Response should contain 'id' field and must be an integer"
            assert "token" in response.json() and type(
                response.json()["token"] == str), "Response should contain 'token' field and must be a string"

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating user: {e}")
            assert False

    def test_should_not_create_a_new_user_when_pass_an_empty_user_email(self):
        """Should create a new user when pass an empty user email"""

        VALID_BODY = generate_user_data_json(self.loaded_schema)
        # turn empty the email parameter
        modify_json_values(VALID_BODY, "email", "")
        try:
            response = requests.post(self.URL_REQRES, json=VALID_BODY)
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating user: {e}")
            assert False

    def test_should_not_create_a_new_user_when_pass_an_empty_user_password(self):
        """Should create a new user when pass an empty user email"""

        VALID_BODY = generate_user_data_json(self.loaded_schema)
        # turn empty the email parameter
        modify_json_values(VALID_BODY, "password", "")
        try:
            response = requests.post(self.URL_REQRES, json=VALID_BODY)
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating user: {e}")
            assert False

    def test_should_not_create_a_new_user_when_pass_a_sequence_of_space_user_email(self):
        """Should create a new user when pass an empty user email"""

        VALID_BODY = generate_user_data_json(self.loaded_schema)
        # turn empty the email parameter
        modify_json_values(VALID_BODY, "email", "      ")
        try:
            response = requests.post(self.URL_REQRES, json=VALID_BODY)
            print(response.text)
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating user: {e}")
            assert False

    def test_should_not_create_a_new_user_when_pass_a_sequence_of_space_user_password(self):
        """Should create a new user when pass an empty user email"""

        VALID_BODY = generate_user_data_json(self.loaded_schema)
        # turn empty the email parameter
        modify_json_values(VALID_BODY, "password", "   ")
        try:
            response = requests.post(self.URL_REQRES, json=VALID_BODY)
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating user: {e}")
            assert False