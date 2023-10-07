import requests


def test_get_pets_by_status():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=pending'
    response = requests.get(url=url)
    print(response.json())
