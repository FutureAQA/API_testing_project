import requests


def test_get_pets_by_status_code():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=pending'
    response = requests.get(url=url)
    assert response.status_code == 200, "Wrong status code"


def test_get_pets_headers():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=pending'
    response = requests.get(url=url)
    print(response.headers)
