import pytest
import requests 

url = "https://petstore3.swagger.io/api/v3"
status_ok = 200

def test_can_place_an_order():
    payload = {
        "id": 100,
        "petId": 1987729,
        "quantity": 9,
        "shipDate": "2024-10-18T06:13:20.427Z",
        "status": "approved",
        "complete": True,
    }
    response = requests.post(url + '/store/order', json=payload)
    assert response.status_code == status_ok

    data = response.json()
    print(data)