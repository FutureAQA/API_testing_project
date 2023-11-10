import pytest
import requests
from data.data_kate.data_kate import AllData
from data.data_kate.data_kate import PetUrl
from src.utils.http_methods import MyRequests
import allure
from pprint import pprint
from tests.test_kate.assertions import Assertion
from data.data_kate.data_kate import StatusCode



@allure.epic("Test get pets")
class TestsGetPets:
    assertion = Assertion()
    status_code = StatusCode()
    url = PetUrl


    @allure.title("test_get_pets_is_json")
    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_is_json(self, status):
        url = self.url.URL_PET_STATUS
        response = MyRequests().get(url, status)
        self.assertion.assert_response_is_json(response)

    @allure.title("test_get_pets_by_status")
    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_by_status(self, status):
        url = self.url.BASE_URL + self.url.URL_PET_STATUS
        data = {'status': status, 'limit': 3}
        response = requests.get(url, data)
        self.assertion.assert_status_code(response, self.status_code.OK)


    @allure.title("test_get_pets_check_status")
    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_check_status(self, status):
        url = self.url.BASE_URL + self.url.URL_PET_STATUS
        data = {'status': status}
        response = requests.get(url, data)
        list_item = response.json()
        for item in list_item:
            assert item['status'] == status

    @allure.title("test_get_pets_check_keys")
    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_check_keys(self, status):
        url = self.url.BASE_URL + self.url.URL_PET_STATUS
        response = requests.get(url, status)
        item_list = response.json()
        self.assertion.assert_keys_in_response(item_list, AllData.PET_KEYS_TO_CHECK)
