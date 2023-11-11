from data.data_kate.data_kate import PetUrl
from tests.test_kate.generator.generator import generated_person
import pytest
import requests


@pytest.fixture(scope="function")
def create_and_delete_user():
    person_info = next(generated_person())
    response = requests.post(PetUrl.BASE_URL + PetUrl.URL_USER, json=person_info)
    yield person_info
    delete_url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}"
    response_del = requests.delete(delete_url, json=person_info)
