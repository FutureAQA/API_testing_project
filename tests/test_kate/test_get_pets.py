import pytest
import requests
from data.data_kate.data_kate import AllData
from data.data_kate.data_kate import PetUrl
from src.utils.http_methods import MyRequests
import allure


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
        assert response.status_code == 200
