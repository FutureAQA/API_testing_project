from typing import List
from src.utils.schemas.users.user_schemas import User
from pydantic import ValidationError, TypeAdapter


UsersList = TypeAdapter(List[User])

data = [
    {
        "id": 10,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    },
    {
        "id": 10,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
        "phone": "12345",
        "userStatus": 1
    }
]

try:
    a = UsersList.validate_python(data)
    print(a)
except ValidationError as e:
    print("Error:", e)
    print(e.json())

