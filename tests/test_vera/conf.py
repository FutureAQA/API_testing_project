"""This section contains fixtures for tests"""

import pytest
import random
from tests.test_vera.data.data_pets import random_status, pet_names, get_breed



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
