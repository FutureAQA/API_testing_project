from random import randint
from faker import Faker

faker_eng = Faker("En")
Faker.seed()


def generated_person():
    yield dict(
        id=randint(2000, 5000),
        username=faker_eng.user_name(),
        firstName=faker_eng.first_name(),
        lastName=faker_eng.last_name(),
        email=faker_eng.email(),
        password=randint(100000, 999999),
        phone=faker_eng.phone_number(),
        userStatus=randint(1, 3)
    )