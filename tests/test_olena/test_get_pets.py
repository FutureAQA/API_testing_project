import requests

def test_get_pets_by_status_available():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
    response = requests.get(url=url)
    print(response.json())
    assert response.status_code == 200
