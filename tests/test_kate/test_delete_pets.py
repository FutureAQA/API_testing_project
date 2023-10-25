from src.utils.http_methods import MyRequests
from data.data_kate.data_kate import PetUrl
import requests
import allure


@allure.epic('Test delete pets')
class TestDeletePets:

    url = PetUrl

    @allure.title('test_delete_pet')
    def test_delete_pet(self):
        url = f'{self.url.URL_PET}/13876545'
        response = MyRequests().delete(url)
        assert response.status_code == 200, f'Status code is not 200, status code is {response.status_code}'

    @allure.title('test_delete_pet_has_text')
    def test_delete_pet_has_text(self):
        url = f'{self.url.URL_PET}/13876545'
        response = MyRequests().delete(url)
        assert response.text == 'Pet deleted', 'Wrong text'

    @allure.title('test_delete_deleted_pet')
    def test_delete_deleted_pet(self):
        url = f'{self.url.BASE_URL}{self.url.URL_PET}/13876545'
        response = requests.delete(url)
        print(response.text)
        assert response.status_code == 404, f'Status code is not 404, status code is {response.status_code}'

