import requests


def test_get_pets_is_json():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
    response = requests.get(url=url)
    assert 'application/json' in response.headers.get('Content-Type', '')