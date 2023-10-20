"""This section contains fixtures for tests"""

import pytest
import random
from tests.test_vera.data.data_pets import random_status, pet_names
from tests.test_vera.generator.generator import Pet, get_breed

@pytest.fixture
def schema():
    return {
        "id": 10,
        "name": "doggie",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
              "id": 0,
              "name": "string"
            }
        ],
        "status": "available"
    }

@pytest.fixture
def headers():
    return {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

@pytest.fixture
def headers_xml():
    return {
            "accept": "application/xml",
            "Content-Type": "application/json"
        }


@pytest.fixture
def pet_data():
    return{
        "name": random.choice(pet_names),
        "photoUrls": [
            "https://example.com/image1.jpg"
        ],
        "id": str(92233720169000) + str(random.randint(10000, 99999)),
        "category": {
            "id": random.randint(1, 99999999),
            "name": get_breed()
        },
        "tags": [
            {
                "id": random.randint(1, 999999),
                "name": get_breed()
            },
            {
                "id": random.randint(1, 99999999),
                "name": get_breed()
            }
        ],
        "status": random_status
    }
