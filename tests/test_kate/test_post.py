import json
from src.utils.http_methods import MyRequests
from data.data_kate.data_kate import PetUrl


def file_read(file):
    f = open(file, 'r', encoding='utf-8')
    j = json.load(f)
    return j


class TestPostPets:
    url = PetUrl

    def test_create_new_pet(self):
        url = self.url.URL_PET
        j = file_read('../../data/data_kate/body_new_pet.json')
        response = MyRequests().post(url, data=j)
        assert response.status_code == 200, "Status_code is not 200"
