import allure
from src.utils.http_methods import MyRequests
from data.data_kate.data_kate import PetUrl
from tests.test_kate.utils import file_read


@allure.epic("Test update pet")
class TestUpdatePets:
    url = PetUrl

    @allure.title("test_update_pet")
    def test_update_pet(self):
        url = self.url.URL_PET
        j = file_read('data/data_kate/body_update_pet.json')
        response = MyRequests().put(url, data=j)
        assert response.status_code == 200, "Status_code is not 200"
