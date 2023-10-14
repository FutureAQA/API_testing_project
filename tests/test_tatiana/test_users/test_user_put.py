import requests
import pytest
from tests.test_tatiana.data.urls import Urls
from tests.test_tatiana.data.data import *

class Test_users_put:

    def test_update_users_positive(self):
        url_post = f'{Urls.BASE_URL}{Urls.CREATE_USER}'
        requests.post(url_post, json=data_user)
        url_get = f'{Urls.BASE_URL}{Urls.USER}{username}'
        response_get = requests.get(url_get)
        assert username == response_get.json()['username']
        url_put = f'{Urls.BASE_URL}{Urls.USER}{username_put}'
        requests.put(url_put, json=data_user_put)
        get_check = requests.get(url_put)
        assert username_put == get_check.json()['username']

    def test_update_users_negative(self):
        url_put = f'{Urls.BASE_URL}{Urls.USER}'
        response_put = requests.put(url_put, json=data_user_put)
        assert response_put.status_code == 405, "Wrong status code"

