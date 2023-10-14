import requests
import pytest
from tests.test_tatiana.data.urls import Urls
from tests.test_tatiana.data.data import *

class Test_users_get:

    def test_get_users_by_username_positive(self):
        url_post = f'{Urls.BASE_URL}{Urls.CREATE_USER}'
        requests.post(url_post, json=data_user)
        url_get = f'{Urls.BASE_URL}{Urls.USER}{username}'
        response_get = requests.get(url_get)
        assert response_get.status_code == 200, "Wrong status code"

    def test_get_users_by_non_existent_username_negative(self):
        a = generate_random_string()
        url_get_negative = f"{Urls.BASE_URL}{Urls.USER}{a}"
        response = requests.get(url_get_negative)
        assert response.status_code == 404, "Wrong status code"


    def test_get_users_by_empty_username__negative(self):
        url_get = f'{Urls.BASE_URL}{Urls.USER}'
        response_get = requests.get(url_get)
        assert response_get.status_code == 405, "Wrong status code"