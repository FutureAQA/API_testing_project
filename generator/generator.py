"""
This file is used to generate fake data
"""
import random
from data.data import Store, Pet, PetCategoryAndTagsName
from faker import Faker
from data.pet_data import PetName, PetBread

faker_en = Faker('En')
Faker.seed()
pet_name = PetName()
pet_bread = PetBread()


def get_status_store():
    """
    This method returns a random status
    :return: placed, approved  or delivered
    """
    return random.choice(["placed", "approved", "delivered"])


def get_status_pet():
    """
    This method returns a random status
    :return: available, pending or sold
    """
    return random.choice(["available", "pending", "sold"])


def get_bool():
    """
    This method returns a random boolean
    :return: True or False
    """
    return random.choice([True, False])


def get_random_int():
    """
    This method returns a random integer
    :return: number between 100 and 999999
    """
    return random.randint(100, 999999)


def generated_store():
    """
    This method returns a store
    :return: data of Store class
    """
    yield Store(
        uid=get_random_int(),
        pet_id=get_random_int(),
        quantity=get_random_int(),
        ship_date=faker_en.iso8601(),
        status=get_status_store(),
        complete=get_bool()
    )


def generated_pet():
    """
    This method returns a pet
    :return: data of Pet class
    """
    yield Pet(
        uid=get_random_int(),
        category={"id": get_random_int(), "name": pet_name.get_pet_name()},
        name=pet_bread.get_bread(),
        photo_urls=faker_en.image_url(),
        tags={"id": get_random_int(), "name": faker_en.word()},
        status=get_status_pet()
    )


def generated_pet_tags_and_category():
    """
    This method returns a pet category and tags
    :return: data of PetCategoryAndTagsName class
    """
    yield PetCategoryAndTagsName(
        category_name=pet_name.get_pet_name(),
        tags_name=faker_en.word()
    )


def generate_fake_dict():
    """
    This method returns a random dictionary
    :return: random dict
    """
    random_dict = faker_en.pydict(nb_elements=1)
    return random_dict
