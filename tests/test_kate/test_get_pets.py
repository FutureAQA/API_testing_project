import pytest
from data.data_kate.data_kate import AllData
from data.data_kate.data_kate import PetUrl
from src.utils.http_methods import MyRequests


class TestsGetPets:
    url = PetUrl
    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_is_json(self, status):
        url = self.url.URL_PET_STATUS
        response = MyRequests().get(url, status)
        assert 'application/json' in response.headers.get('Content-Type', '')


    @pytest.mark.parametrize("status", AllData.PETS_STATUS)
    def test_get_pets_by_status(self, status):
        # url = f'{AllData.URL_PET_STATUS}{status}'
        url = self.url.URL_PET_STATUS
        response = MyRequests().get(url, status)
        assert response.status_code == 200
