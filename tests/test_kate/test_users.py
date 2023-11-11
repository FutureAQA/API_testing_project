import requests
from data.data_kate.data_kate import PetUrl
from tests.test_kate.generator.generator import generated_person
from src.utils.http_methods import MyRequests
from tests.test_kate.assertions import Assertion
from data.data_kate.data_kate import StatusCode
from tests.test_kate.confest_kate import create_and_delete_user
from data.data_kate.data_kate import AllData
from tests.test_kate.pages.page_user import update_user_data
import allure


@allure.epic("Tests for users")
class TestCreateUsers:
    assertion = Assertion()
    url = PetUrl
    status_code = StatusCode()
    key = AllData

    @allure.title("test_create_user_check_status_code")
    def test_create_user_check_status_code(self, create_and_delete_user):
        person_info = create_and_delete_user
        url = self.url.BASE_URL + self.url.URL_USER
        response = requests.post(url, json=person_info)
        # response = MyRequests().post('user', data=person_info) // for version 3
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title("test_create_user_check_message")
    def test_create_user_check_message(self, create_and_delete_user):
        person_info = create_and_delete_user
        url = self.url.BASE_URL + self.url.URL_USER
        response = requests.post(url, json=person_info)
        # response = MyRequests().post('user', data=person_info) // for version 3
        self.assertion.assert_check_message(response, person_info)

    @allure.title("test_create_user_is_present_in_databas")
    def test_create_user_is_present_in_database(self, create_and_delete_user):
        person_info = create_and_delete_user
        user_url = self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}"
        response_get = requests.get(user_url, json=person_info)
        user_data = response_get.json()
        self.assertion.assert_dicts_values_matches(user_data, person_info)

    @allure.title("test_get_user_check_status_code")
    def test_get_user_check_status_code(self, create_and_delete_user):
        person_info = create_and_delete_user
        response = requests.get(self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}", json=person_info)
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title("test_get_user_check_is_json")
    def test_get_user_check_is_json(self, create_and_delete_user):
        person_info = create_and_delete_user
        response = requests.get(self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}", json=person_info)
        self.assertion.assert_response_is_json(response)

    @allure.title("test_get_user_check_keys")
    def test_get_user_check_keys(self, create_and_delete_user):
        person_info = create_and_delete_user
        response = requests.get(self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}")
        user_data = response.json()
        self.assertion.assert_keys_in_dict(user_data, AllData.USER_KEYS_TO_CHECK)

    @allure.title("test_update_user_check_status_code")
    def test_update_user_check_status_code(self, create_and_delete_user):
        person_info = create_and_delete_user
        updated_person_info = update_user_data(person_info)
        update_url = self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}"
        response = requests.put(update_url, json=updated_person_info)
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title("test_update_user_check_message")
    def test_update_user_check_message(self, create_and_delete_user):
        person_info = create_and_delete_user
        updated_person_info = update_user_data(person_info)
        update_url = self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}"
        response = requests.put(update_url, json=updated_person_info)
        self.assertion.assert_check_message(response, person_info)

    @allure.title("test_update_user_check_value")
    def test_update_user_check_value(self, create_and_delete_user):
        person_info = create_and_delete_user
        updated_person_info = update_user_data(person_info)
        updated_url = self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}"
        response_put = requests.put(updated_url, json=updated_person_info)
        response_get = requests.get(updated_url, json=updated_person_info)
        updated_data = response_get.json()
        self.assertion.assert_check_updated_values(updated_data, updated_person_info)

    @allure.title("test_check_update_username_and_id")
    def test_check_update_username_and_id(self, create_and_delete_user):
        person_info = create_and_delete_user
        updated_person_info = update_user_data(person_info)
        updated_url = self.url.BASE_URL + self.url.URL_USER + f"/{person_info['username']}"
        response_put = requests.put(updated_url, json=updated_person_info)
        response_get = requests.get(updated_url, json=updated_person_info)
        assert response_get.json()['username'] == person_info['username'], 'Username is changed'
        assert response_get.json()['id'] == person_info['id'], 'ID is changed'

