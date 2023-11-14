from data.data_kate.data_kate import PetUrl
from tests.test_kate.generator.generator import generated_person
import pytest
import requests
from tests.test_kate.pages.page_user import update_user_data


@pytest.fixture(scope="function")
def create_and_delete_user():
    person_info = next(generated_person())
    response = requests.post(PetUrl.BASE_URL + PetUrl.URL_USER, json=person_info)
    yield person_info, response
    delete_url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}"
    response_del = requests.delete(delete_url, json=person_info)

# @pytest.fixture(scope="function")
# def create_and_delete_user():
#     person_info = next(generated_person())
#     response = requests.post(PetUrl.BASE_URL + PetUrl.URL_USER, json=person_info)
#     yield response
#     delete_url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}"
#     response_del = requests.delete(delete_url, json=person_info)


@pytest.fixture(scope="function")
def get_info_created_user():
    person_info = next(generated_person())
    response_post = requests.post(PetUrl.BASE_URL + PetUrl.URL_USER, json=person_info)
    return person_info


@pytest.fixture(scope="function")
def get_response_created_user(get_info_created_user):
    person_info = get_info_created_user
    response = requests.get(PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}", json=person_info)
    yield response
    delete_url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}"
    response_del = requests.delete(delete_url, json=person_info)


@pytest.fixture(scope='function')
def get_updated_user_data(get_info_created_user):
    person_info = get_info_created_user
    updated_person_info = update_user_data(person_info)
    update_url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}"
    response = requests.put(update_url, json=updated_person_info)
    yield response, person_info, updated_person_info
    delete_url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}"
    response_del = requests.delete(delete_url, json=person_info)


@pytest.fixture(scope="function")
def get_response_updated_user(get_updated_user_data):
    response, person_info, updated_person_info = get_updated_user_data
    updated_url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{person_info['username']}"
    response_get = requests.get(updated_url, json=updated_person_info)
    return response_get, person_info, updated_person_info
