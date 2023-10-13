import pytest
import requests

from tests.test_nata.constant_nata import ADD_NEW_PET, PET_URL


@pytest.fixture(scope='function')
def add_new_pet():
    url = PET_URL
    response = requests.post(url, json=ADD_NEW_PET)
    return response
