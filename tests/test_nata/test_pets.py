import requests


def test_get_pets_by_status_code():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=pending'
    response = requests.get(url=url)
    print(response.status_code)
    assert response.status_code == 200, "Wrong status code"
