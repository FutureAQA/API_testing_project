import pytest
import requests
from data.data_kate.data_kate import AllData
from data.data_kate.data_kate import PetUrl
from src.utils.http_methods import MyRequests
import allure
from pprint import pprint


@allure.epic("Test get pets")
class TestsGetPets:
    url = PetUrl

    @allure.title("test_get_pets_is_json")
    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_is_json(self, status):
        url = self.url.URL_PET_STATUS
        response = MyRequests().get(url, status)
        assert 'application/json' in response.headers.get('Content-Type', '')

    @allure.title("test_get_pets_by_status")
    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_by_status(self, status):
        url = self.url.BASE_URL + self.url.URL_PET_STATUS
        response = requests.get(url, status)
        assert response.status_code == 200, f"Status code is not 200, status code is {response.status_code}"

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
        for item in item_list:
            assert 'id' in item, "Key 'id' is missing in the response"
            assert 'tag' in item, "Key 'tag' is missing in the response"
            assert 'category' in item, "Key 'category' is missing in the response"
            assert 'name' in item, "Key 'name' is missing in the response"
