import requests
import pytest

PET_URL = 'https://petstore.swagger.io/v2/pet/'
FIND_BY_STATUS = 'findByStatus?status='
ADD_NEW_PET = {
  "id": 777,
  "category": {
    "id": 777,
    "name": "cat"
  },
  "name": "grey",
  "photoUrls": [
      'https://www.novochag.ru/upload/img_cache/120/12032883eda938679ed07b74347b3f07_cropped_1332x1998.webp'
  ],
  "tags": [
    {
      "id": 777,
      "name": "Smok"
    }
  ],
  "status": "available"
}


class TestPet:

    @pytest.mark.parametrize('status', ['pending', 'available', 'sold'])
    def test_get_finds_pets_by_status(self, status):
        url = f'{PET_URL}{FIND_BY_STATUS}{status}'
        response = requests.get(url=url)
        assert response.status_code == 200, "Wrong status code"

    def test_post_add_a_new_pet_to_the_store(self):
        url = PET_URL
        response = requests.post(url, json=ADD_NEW_PET)
        assert response.status_code == 200, "Wrong status code"

    def test_get_pet_by_id(self):
        url = f'{PET_URL}777'
        response = requests.get(url)
        assert response.status_code == 200, "Wrong status code"