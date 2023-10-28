from src.utils.http_methods import MyRequests
from data.data_kate.data_kate import PetUrl
import allure
from tests.test_kate.utils import file_read


@allure.epic("Test post pet")
class TestPostPets:
    url = PetUrl

    @allure.title("test_create_new_pet_check_status_code")
    def test_create_new_pet_check_status_code(self):
        url = self.url.URL_PET
        j = file_read('data/data_kate/body_new_pet.json')
        response = MyRequests().post(url, data=j)
        assert response.status_code == 200, "Status_code is not 200"

    @allure.title("test_create_new_pet")
    def test_create_new_pet(self):
        url = self.url.URL_PET
        j = file_read('data/data_kate/body_new_pet.json')
        response = MyRequests().post(url, data=j)
        assert response.json()['tags'][0]['name'] == j['tags'][0]['name'], 'Name of pet in response is not correct'
        assert response.json()['category']['name'] == j['category']['name'], 'Name of breed in response is not correct'
