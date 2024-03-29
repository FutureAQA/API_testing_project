import requests
from data.data_kate.data_kate import PetUrl
from tests.test_kate.generator.generator import generated_person
from src.utils.http_methods import MyRequests
from tests.test_kate.assertions import MyAssertion
from src.utils.assertions import Assertion
from data.data_kate.data_kate import StatusCode
from tests.test_kate.confest_kate import *
from data.data_kate.data_kate import AllData
from tests.test_kate.pages.page_user import TestUser
import allure


@allure.epic("Tests for users")
class TestCreateUsers:
    assertion = MyAssertion()
    assertions = Assertion()
    url = PetUrl
    status_code = StatusCode()
    key = AllData
    test_user = TestUser()

    @allure.title("test_create_user_check_status_code")
    def test_create_user_check_status_code(self, create_and_delete_user):
        person_info, response = create_and_delete_user
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title("test_create_user_check_message")
    def test_create_user_check_message(self, create_and_delete_user):
        person_info, response = create_and_delete_user
        self.assertion.assert_check_key_message(response, person_info['id'])

    @allure.title("test_create_user_is_present_in_database")
    def test_create_user_is_present_in_database(self, get_response_created_user, get_info_created_user):
        person_info = get_info_created_user
        user_data = get_response_created_user.json()
        self.assertion.assert_dicts_values_matches(user_data, person_info)

    @allure.title("test_get_user_check_status_code")
    def test_get_user_check_status_code(self, get_response_created_user):
        response = get_response_created_user
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title("test_get_user_check_is_json")
    def test_get_user_check_is_json(self, get_response_created_user):
        response = get_response_created_user
        self.assertion.assert_response_is_json(response)

    @allure.title("test_get_user_check_keys")
    def test_get_user_check_keys(self, get_response_created_user):
        user_data = get_response_created_user.json()
        self.assertion.assert_keys_in_dict(user_data, AllData.USER_KEYS_TO_CHECK)

    @allure.title("test_update_user_check_status_code")
    def test_update_user_check_status_code(self, get_updated_user_data):
        response, person_info, updated_person_info = get_updated_user_data
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title("test_update_user_check_message")
    def test_update_user_check_message(self, get_updated_user_data):
        response, person_info, updated_person_info = get_updated_user_data
        self.assertion.assert_check_key_message(response, person_info['id'])


    @allure.title("test_update_user_check_value")
    def test_update_user_check_value(self, get_response_updated_user):
        response_get, person_info, updated_person_info = get_response_updated_user
        updated_data = response_get.json()
        self.assertion.assert_check_updated_values(updated_data, updated_person_info)

    @allure.title("test_check_update_username_and_id")
    def test_check_update_username_and_id(self, get_response_updated_user):
        response_get, person_info, updated_person_info = get_response_updated_user
        assert response_get.json()['username'] == person_info['username'], 'Username is changed'
        assert response_get.json()['id'] == person_info['id'], 'ID is changed'


    @allure.title("test_delete_user_status_code")
    def test_delete_user_status_code(self, get_info_created_user):
        response = self.test_user.delete_user(get_info_created_user['username'])
        self.assertions.assert_status_code(response, self.status_code.OK)

    @allure.title("test_delete_user_response")
    def test_delete_user_response(self, get_info_created_user):
        response = self.test_user.delete_user(get_info_created_user['username'])
        self.assertion.assert_check_key_message(response, get_info_created_user['username'])

    @allure.title("test_delete_deleted_users_has_status_code_404")
    def test_delete_deleted_users_has_status_code_404(self, get_info_created_user):
        self.test_user.delete_user(get_info_created_user['username'])
        response_del = self.test_user.delete_user(get_info_created_user['username'])
        self.assertions.assert_status_code(response_del, self.status_code.NOT_FOUND)


