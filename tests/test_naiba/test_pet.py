import allure_commons
import pytest
import requests 

url = "https://petstore3.swagger.io/api/v3"
status_ok = 200

def test_can_call_endpoint():
    response = requests.get(url)
    assert response.status_code == status_ok
    pass  

@allure_commons.title("test_get_pets_by_status")
def test_get_pets_by_status():
    response = requests.get("https://petstore3.swagger.io/api/v3/pet/findByStatus?status=sold")
    print(response.json())
    assert response.status_code == status_ok

def test_add_new_pet():
    payload = {
        "id": 9999,
        "name": "lucky",
        "category": {
            "id": 9999,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 9999,
            "name": "lucky"
            }
        ],
        "status": "available"
    }
    add_pet_response = requests.post(url + "/pet", json=payload)
    assert add_pet_response.status_code == status_ok
    
    #id = response.json()['id']
    #get_response = requests.get(f'{url}/{id}')
    #assert get_response.json()['name'] == 'lucky'

    data = add_pet_response.json()
    print(data)








