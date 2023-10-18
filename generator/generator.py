import random
from data.data import Store
from faker import Faker


faker_en = Faker('En')
Faker.seed()


def get_status():
    return random.choice(["placed", "approved", "delivered"])


def get_bool():
    return random.choice([True, False])


def generated_store():
    yield Store(
        uid=random.randint(100, 999999),
        pet_id=random.randint(100, 999999),
        quantity=random.randint(1, 9999),
        ship_date=faker_en.iso8601(),
        status=get_status(),
        complete=get_bool()
    )
