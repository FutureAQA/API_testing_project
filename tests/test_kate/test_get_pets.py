import requests
import pytest
from data.urls import Urls
from tests.test_kate.data_kate import AllData


def test_get_pets_is_json():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
    response = requests.get(url=url)
    assert 'application/json' in response.headers.get('Content-Type', '')


@pytest.mark.parametrize("status", AllData.pets_status)
def test_get_pets_by_status(status):
    url = f'/pet/findByStatus?status={status}'
    response = requests.get(f'{Urls.BASE_URL}{url}')
    assert response.status_code == 200