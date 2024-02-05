import logging

import requests
from src.config import URL_REQRES
from src.service.create_user import create_user
from precisely import assert_that, is_sequence

from src.service.file_reader import file_reader
from src.service.generate_schema.generate_json_from_schema import generate_user_data_json
from src.service.global_var import EMPTY_VAR, SEQUENCE_OF_SPACE_VAR, NON_EXISTENT_ID
from src.service.list_user import list_user


class TestUpdateUsers:
    def setup_class(self):
        self.loaded_schema = file_reader(filename='../service/generate_schema/update_user_details.json')

    def test_should_update_all_users_details_when_pass_a_valid_user_id(self):

        VALID_BODY = generate_user_data_json(self.loaded_schema)
        print("This is the body that will be used to update the user details \n", VALID_BODY)
        # Create and get user id
        USER_ID = create_user()
        print("This is the user id", USER_ID)
        USERS_LIST = list_user(user_id=USER_ID)
        print("User details before update", USERS_LIST)
        response = requests.patch(f'{URL_REQRES}/users/{USER_ID}', json=VALID_BODY)
        print("This is the body responded after update", response.json())
        USERS_LIST = list_user(user_id=USER_ID)
        print("User details after update", USERS_LIST)
        assert response.status_code == 200
