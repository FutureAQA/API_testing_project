import requests


def test_get_pets_by_status():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    response = requests.get(url=url)
    print(response.json())

test_get_pets_by_status()
