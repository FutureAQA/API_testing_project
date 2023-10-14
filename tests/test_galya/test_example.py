import os

import pytest
import requests


def test_get_find_pets_by_status_pending():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=pending'
    response = requests.get(url=url)
    print(response.json())


def test_get_find_pets_by_status_sold():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
    response = requests.get(url=url)
    print(response.json())


@pytest.mark.xfail
def test_get_find_pets_by_id():
    url = 'https://petstore.swagger.io/v2/pet/12'
    response = requests.get(url=url)
    assert response.status_code == 200, "Wrong status code"
    print(response.json())


def test_get_user_by_user_name():
    url = 'https://petstore.swagger.io/v2/user/Polkan'
    response = requests.get(url=url)
    print(response.json())


def test_get_purchase_by_id():
    url = 'https://petstore.swagger.io/v2/store/order/9'
    response = requests.get(url=url)
    assert response.status_code == 404, "Wrong status code"
    print(response.json())
