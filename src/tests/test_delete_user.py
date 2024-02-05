import requests
from src.config import URL_REQRES
from src.service.create_user import create_user
from precisely import assert_that, is_sequence
from src.service.global_var import EMPTY_VAR, SEQUENCE_OF_SPACE_VAR, NON_EXISTENT_ID
from src.service.list_user import list_user


class TestDeleteUsers:
    def test_should_delete_user_when_pass_a_valid_user_id(self):
        # Create and get user id
        USER_ID = create_user()
        # Delete user
        response = requests.delete(f'{URL_REQRES}/users/{USER_ID}')
        assert response.status_code == 204

    def test_should_remove_user_from_data_base_after_delete_user_when_a_valid_user_id(self):
        # Create and get user id
        USER_ID = create_user()
        # Delete user
        delete_user = requests.delete(f'{URL_REQRES}/users/{USER_ID}')
        assert delete_user.status_code == 204
        USERS_LIST = list_user(user_id=USER_ID)
        assert USER_ID not in USERS_LIST

    def test_should_not_delete_user_when_pass_an_empty_user_id(self):
        # Delete user
        response = requests.delete(f'{URL_REQRES}/users/{EMPTY_VAR}')
        assert response.status_code == 400

    def test_should_not_delete_user_when_pass_a_sequence_of_space_user_id(self):
        # Delete user
        response = requests.delete(f'{URL_REQRES}/users/{SEQUENCE_OF_SPACE_VAR}')
        assert response.status_code == 400

    def test_should_not_delete_user_when_pass_a_non_existend_user_id(self):
        # Delete user
        response = requests.delete(f'{URL_REQRES}/users/{NON_EXISTENT_ID}')
        assert response.status_code == 404
