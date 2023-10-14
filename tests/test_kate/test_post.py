import requests

URL_NEW_PET = 'https://petstore.swagger.io/v2/pet'
BODY_NEW_PET = {
    "id": 135,
    "category": {
        "id": 135,
        "name": "Dog"
    },
    "name": "white",
    "photoUrls": [
        "https://irko-ingur.ru/thumb/2/CjW1zeDt5rlzue4SyUFFMQ/r/d/iork.jpg"
    ],
    "tags": [
        {
            "id": 135,
            "name": "Eazy"
        }
    ],
    "status": "available"
}


def test_create_new_pet():
    url = URL_NEW_PET
    response = requests.post(url, json=BODY_NEW_PET)
    assert response.status_code == 200, "Status_code is not 200"
