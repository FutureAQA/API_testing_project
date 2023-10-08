from typing import Optional
import validators

from pydantic import BaseModel, ValidationError, field_validator, PositiveInt, root_validator, validator
from pydantic_core.core_schema import ValidationInfo


class Tags(BaseModel):
    id: PositiveInt
    name: str


class Category(BaseModel):
    id: int = 0
    name: str


class Pets(BaseModel):
    id: PositiveInt
    name: str
    category: Category
    photoUrls: Optional[list[str]] = []
    tags: list[Tags]
    status: str

    @field_validator("photoUrls")
    @classmethod
    def check_photo_urls(cls, v: list[str]) -> list[str]:
        for url in v:
            if not validators.url(url):
                raise ValueError("photoUrls must be a list of urls or empty")
        return v

    @field_validator("status")
    @classmethod
    def check_status(cls, v: str) -> str:
        if v in ["available", "pending", "sold"]:
            return v
        raise ValueError(f"Your status is {v}. Status must be available, pending or sold")


data = """
{
    "id": 1,
    "category": {
        "id": 2,
        "name": "Masha"
    },
    "name": "doggie",
        "photoUrls": ["https://hello.com", "https://world.ru"],
    "tags": [
        {
            "id": 2,
            "name": "name"
        },
        {
            "id": 3,
            "name": "name"
        }
    ],
    "status": "sold"
}
"""
try:
    pets = Pets.model_validate_json(data)
    print(pets.model_dump_json())
except ValidationError as e:
    print("Error")
    print(e.json())

# "https://hello.com",
# "https://world.ru"
