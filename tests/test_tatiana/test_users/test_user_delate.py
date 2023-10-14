import requests
import pytest
from tests.test_tatiana.data.urls import Urls
from tests.test_tatiana.data.data import *

class Test_user_delate:
    def test_delate_user_by_user_name_positive(self):
        url_post = f'{Urls.BASE_URL}{Urls.CREATE_USER}'
        response_post = requests.post(url_post, json=data_user)
        url_delate = f'{Urls.BASE_URL}{Urls.USER}{username}'
        response_delate = requests.delete(url_delate)
        assert response_delate.status_code == 200, "Wrong status code"

    def test_delate_users_by_empty_username_negative(self):
        url_delate = f'{Urls.BASE_URL}{Urls.USER}'
        response_delate = requests.delete(url_delate)
        assert response_delate.status_code == 405, "Wrong status code"

    def test_delate_users_by_non_existent_username_negative(self):
        a = generate_random_string()
        print(a)
        url_delate_negative = f"{Urls.BASE_URL}{Urls.USER}{a}"
        response = requests.get(url_delate_negative)
        assert response.status_code == 404, "Wrong status code"