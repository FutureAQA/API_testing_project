import random
from data.data import Store, Pet
from faker import Faker
from data.pet_data import PetName, PetBread

faker_en = Faker('En')
Faker.seed()
pet_name = PetName()
pet_bread = PetBread()


def get_status_store():
    return random.choice(["placed", "approved", "delivered"])


def get_status_pet():
    return random.choice(["available", "pending", "sold"])


def get_bool():
    return random.choice([True, False])


def generated_store():
    yield Store(
        uid=random.randint(100, 999999),
        pet_id=random.randint(100, 999999),
        quantity=random.randint(1, 9999),
        ship_date=faker_en.iso8601(),
        status=get_status_store(),
        complete=get_bool()
    )


def generated_pet():
    yield Pet(
        uid=random.randint(100, 999999),
        category={"id": random.randint(100, 999999), "name": pet_name.get_pet_name()},
        name=pet_bread.get_bread(),
        photo_urls=faker_en.image_url(),
        tags={"id": random.randint(100, 999999), "name": faker_en.word()},
        status=get_status_pet()
    )
