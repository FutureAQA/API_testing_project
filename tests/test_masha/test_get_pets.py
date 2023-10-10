import requests

def test_get_pets_by_status_available():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
    response = requests.get(url=url)
    print(response.json())

def test_get_pets_by_status_pending():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=pending'
    response = requests.get(url=url)
    print(response.json())

def test_get_pets_by_status_sold():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
    response = requests.get(url=url)
    print(response.json())


def test_get_pets_by_status_error_adress():
    url = 'https://petstore.swagger.io/pet/findByStatus?status=sold'
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Ошибка: Получен статус код {response.status_code}")
