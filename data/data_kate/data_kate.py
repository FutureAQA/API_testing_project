from dataclasses import dataclass


class AllData:
    PETS_STATUS = ['available', 'pending', 'sold']
    USER_KEYS_TO_CHECK = ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus']
    PET_KEYS_TO_CHECK = ['id', 'tag', 'category', 'name']
    PETS_REQUIRED_KEYS = ['id', 'name', 'status']
    PET_OPTIONAL_KEYS = ['category', 'photoUrls', 'tags']




class PetUrl:
    URL_PET = 'pet'
    URL_PET_STATUS = 'pet/findByStatus'
    BASE_URL = "https://petstore.swagger.io/v2/"
    URL_USER = 'user'




@dataclass
class User:
    id: int = None
    username: str = None
    firstName: str = None
    lastName: str = None
    email: str = None
    password: str = None
    phone: int = None
    userStatus: int = None


class StatusCode:
    OK = 200
    INVALID_USERNAME = 400
    NOT_FOUND = 404


