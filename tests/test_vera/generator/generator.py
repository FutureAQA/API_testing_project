"""  This module includes methods for generating test data used in API endpoint testing."""
import random
import uuid
from tests.test_vera.data.data import Pet, User
from tests.test_vera.data.data_pets import pet_names, dog_breeds, cat_breeds


def get_breed():
    all_breed = dog_breeds + cat_breeds
    return random.choice(all_breed)


def generated_pet():
    yield Pet(
        id_number= random.randint(1, 10000),
        name=random.choice(pet_names),
        photoUrls=generate_random_photo_url(),
        status=random.choice(["available", "pending", "sold"]),
        breed=get_breed()
    )

def generate_random_photo_url():
    base_url = "https://example.com/images/"
    image_name = str(uuid.uuid4())
    full_image_url = f"""{base_url}{image_name}.jpg"""
    return full_image_url


pet_data = next(generated_pet())
pet = {
    "pet_id": str(92233720169000) + str(random.randint(10000, 99999)),
    "pet_name": pet_data.name,
    "photo_urls": pet_data.photoUrls,
    "pet_status": pet_data.status,
    "pet_breed": pet_data.breed,
}
