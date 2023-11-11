from src.utils.http_methods import MyRequests
from data.data_kate.data_kate import PetUrl
import allure
from tests.test_kate.utils import file_read
from tests.test_kate.assertions import Assertion
from data.data_kate.data_kate import StatusCode


@allure.epic("Test post pet")
class TestPostPets:
    assertion = Assertion()
    status_code = StatusCode()
    url = PetUrl

    @allure.title("test_create_new_pet_check_status_code")
    def test_create_new_pet_check_status_code(self):
        url = self.url.URL_PET
        j = file_read('data/data_kate/body_new_pet.json')
        response = MyRequests().post(url, data=j)
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title("test_create_new_pet")
    def test_create_new_pet(self):
        url = self.url.URL_PET
        j = file_read('data/data_kate/body_new_pet.json')
        response = MyRequests().post(url, data=j)
        assert response.json()['tags'][0]['name'] == j['tags'][0]['name'], 'Name of pet in response is not correct'
        assert response.json()['category']['name'] == j['category']['name'], 'Name of breed in response is not correct'

    
