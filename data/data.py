"""
This file defines a set of data classes representing entities related to a store and pets.
Each data class is annotated using the dataclass decorator from the dataclasses module,
providing a concise way to define classes for storing data
"""

from dataclasses import dataclass


@dataclass
class BaseData:
    uid: int = None


@dataclass
class Store(BaseData):
    pet_id: int = None,
    quantity: int = None,
    ship_date: str = None,
    status: str = None,
    complete: bool = None


@dataclass
class Pet(BaseData):
    category: dict = None,
    name: str = None,
    photo_urls: str = None,
    tags: dict = None,
    status: str = None


@dataclass
class User(BaseData):
    user_name: str = None,
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    password: str = None,
    phone: str = None,
    user_status: int = None


@dataclass
class PetCategoryAndTagsName(BaseData):
    category_name: str = None,
    tags_name: str = None
