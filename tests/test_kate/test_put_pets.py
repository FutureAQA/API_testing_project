import allure
from src.utils.http_methods import MyRequests
from data.data_kate.data_kate import PetUrl
from tests.test_kate.utils import file_read


@allure.epic("Test update pet")
class TestUpdatePets:
    url = PetUrl

    @allure.title("test_update_pet_check_status_code")
    def test_update_pet_check_status_code(self):
        url = self.url.URL_PET
        j = file_read('data/data_kate/body_update_pet.json')
        response = MyRequests().put(url, data=j)
        assert response.status_code == 200, "Status_code is not 200"

    @allure.title("test_update_pet")
    def test_update_pet(self):
        url = self.url.URL_PET
        j = file_read('data/data_kate/body_update_pet.json')
        response = MyRequests().put(url, data=j)
        assert response.json()['tags'][0]['name'] != 'Eazy', 'Name of pet is not update'
        assert response.json()['category']['name'] != 'dog', 'Name of breed is not update'

