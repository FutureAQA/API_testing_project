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
