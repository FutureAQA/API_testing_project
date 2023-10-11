import requests
import pytest
import string
import random

class Test_users_get:
    data = [
        {
            'id': 3434,
            'username': 'Garry44545',
            'firstName': 'Garry4',
            'lastName': 'Garry4',
            'email': 'rt@we',
            'password': '123'
        }
    ]
    username = data[0]['username']
    def test_get_users_by_username_positive(self):
        url_post = 'https://petstore.swagger.io/v2/user/createWithArray'
        response_post = requests.post(url_post, json=self.data)
        url_get = f'https://petstore.swagger.io/v2/user/{self.username}'
        response_get = requests.get(url_get)
        assert response_get.status_code == 200, "Wrong status code"

    def test_get_users_by_username_negative(self):
        def generate_random_string(length=9):
            letters = string.ascii_lowercase
            rand_string = ''.join(random.choice(letters) for i in range(length))
            return rand_string
        a = generate_random_string()
        url_get_negative = f"https://petstore.swagger.io/v2/user/{a}"
        response = requests.get(url_get_negative)
        assert response.status_code == 404, "Wrong status code"


    def test_get_users_by_empty_username(self):
        url_get = f'https://petstore.swagger.io/v2/user/'
        response_get = requests.get(url_get)
        assert response_get.status_code == 405, "Wrong status code"