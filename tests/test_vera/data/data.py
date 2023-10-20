from dataclasses import dataclass


@dataclass
class Pet:
    id_number: int = None
    name: str = None
    photoUrls: str = None
    status: str = None
    breed: str = None


@dataclass
class User:
    id: int = None
    username: str = None
    firstName: str = None
    lastName: str = None
    email: str = None
    password: str = None
    phone: str = None
    userStatus: int = None
