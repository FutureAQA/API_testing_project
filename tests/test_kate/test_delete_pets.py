from src.utils.http_methods import MyRequests
from data.data_kate.data_kate import PetUrl
import requests
import allure
from tests.test_kate.assertions import Assertion
from data.data_kate.data_kate import StatusCode


@allure.epic('Test delete pets')
class TestDeletePets:

    assertion = Assertion()
    status_code = StatusCode
    url = PetUrl

    @allure.title('test_delete_pet')
    def test_delete_pet(self):
        url = f'{self.url.URL_PET}/13876545'
        response = MyRequests().delete(url)
        self.assertion.assert_status_code(response, self.status_code.OK)

    @allure.title('test_delete_pet_has_text')
    def test_delete_pet_has_text(self):
        url = f'{self.url.URL_PET}/13876545'
        response = MyRequests().delete(url)
        actual_text = response.text
        self.assertion.assert_text(actual_text, 'Pet deleted')

    @allure.title('test_delete_deleted_pet')
    def test_delete_deleted_pet(self):
        url = f'{self.url.BASE_URL}{self.url.URL_PET}/13876545'
        response = requests.delete(url)
        self.assertion.assert_status_code(response, self.status_code.NOT_FOUND)

