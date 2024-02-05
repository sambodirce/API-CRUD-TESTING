import requests
from src.config import URL_REQRES
from src.service.create_user import create_user
from precisely import assert_that, is_sequence

from src.service.global_var import EMPTY_VAR, SEQUENCE_OF_SPACE_VAR, NON_EXISTENT_ID


class TestListUsers:
    def test_should_return_all_users_details_when_pass_a_valid_user_id(self):
        # Create and get user id
        USER_ID = create_user()
        response = requests.get(f'{URL_REQRES}/users/{USER_ID}')
        assert response.status_code == 200
        assert USER_ID == response.json()["data"]["id"]
        assert_that(response.json()["data"],
                    is_sequence("id",
                                "email",
                                "first_name",
                                "last_name",
                                "avatar")), f'body response {response.json}'

    def test_should_return_all_existent_users_details(self):
        # Create and get user id
        response = requests.get(f'{URL_REQRES}/users/{EMPTY_VAR}')
        assert response.status_code == 200
        assert type(response.json()["data"]) is list
        assert len(response.json()["data"]) > 1
        assert_that(response.json(),
                    is_sequence("page",
                                "per_page",
                                "total",
                                "total_pages",
                                "data",
                                "support")), f'body response {response.json}'

    def test_should_return_the_correct_attribute_when_list_all_existent_users_details(self):
        # Create and get user id
        response = requests.get(f'{URL_REQRES}/users/{EMPTY_VAR}')
        assert response.status_code == 200
        assert type(response.json()["data"]) is list
        for i in range(len(response.json()["data"])):
            assert_that(response.json(),
                        is_sequence("page",
                                    "per_page",
                                    "total",
                                    "total_pages",
                                    "data",
                                    "support")), f'body response {response.json}'

    def test_should_not_return_users_details_when_pass_a_sequence_of_space_user_id(self):
        # Create and get user id
        response = requests.get(f'{URL_REQRES}/users/{SEQUENCE_OF_SPACE_VAR}')
        assert response.status_code == 400

    def test_should_not_return_users_details_when_pass_non_existent_user_id(self):
        # Create and get user id
        response = requests.get(f'{URL_REQRES}/users/{NON_EXISTENT_ID}')
        assert response.status_code == 404
