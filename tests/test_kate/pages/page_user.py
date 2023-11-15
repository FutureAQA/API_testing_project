from data.data_kate.data_kate import PetUrl
from tests.test_kate.generator.generator import generated_person
import pytest
import requests



class TestUser:
    @staticmethod
    def update_user_data(person_info):
        update_person_info = next(generated_person())
        update_person_info['id'] = person_info['id']
        update_person_info['username'] = person_info['username']
        return update_person_info

    def delete_user(self, username):
        url = PetUrl.BASE_URL + PetUrl.URL_USER + f"/{username}"
        response = requests.delete(url)
        return response



