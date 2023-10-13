PET_URL = f'https://petstore.swagger.io/v2/pet/'
FIND_BY_STATUS = 'findByStatus?status='

ADD_NEW_PET = {
  "id": 777,
  "category": {
    "id": 777,
    "name": "cat"
  },
  "name": "grey",
  "photoUrls": [
      'https://www.novochag.ru/upload/img_cache/120/12032883eda938679ed07b74347b3f07_cropped_1332x1998.webp'
  ],
  "tags": [
    {
      "id": 777,
      "name": "Smok"
    }
  ],
  "status": "available"
}

UPLOAD_IMAGE = {
  "code": 777,
  "type": "Smoke",
  "message": "file=@Smoke.jpg"
}

UPDATE_PET = {
  "id": 777,
  "category": {
    "id": 777,
    "name": "cat"
  },
  "name": "Smoke",
  "photoUrls": [
    "tests/test_nata/Smoke.jpg"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Puh"
    }
  ],
  "status": "available"
}

