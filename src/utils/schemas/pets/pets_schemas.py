"""
This module contains the schemas for the Pets API
"""

from typing import Optional
import validators
from requests import Response

from src.logger.logger import get_logs
from src.utils.schemas.basic_validator import BasicValidator
from pydantic import BaseModel, ValidationError, field_validator


logger = get_logs(r"src\utils\schemas\pets\pet_schemas")
validator = BasicValidator()


class Tags(BaseModel):
    id: int = 0
    name: Optional[str]


class TagsId(BaseModel):
    id: int = 0


class Category(BaseModel):
    id: int = 0
    name: Optional[str]


class CategoryId(BaseModel):
    id: int = 0


class Pets(BaseModel):
    id: Optional[int]
    name: str
    category: (Category | CategoryId) = None
    photoUrls: Optional[list[str]] = []
    tags: list[Tags | TagsId] = []
    status: str

    @field_validator("photoUrls")
    @classmethod
    def check_photo_urls(cls, v: list[str]) -> list[str]:
        for url in v:
            if not (validators.url(url) or url.startswith("data:image")):
                logger.error(f"Invalid url: {url}")
                raise ValueError("photoUrls must be a list of urls or empty")
        return v

    @field_validator("status")
    @classmethod
    def check_status(cls, v: str) -> str:
        if not validator.is_valid_status(v):
            logger.error(f"Invalid status: {v}")
            raise ValueError(f"Invalid status: {v}. Status must be available, pending, or sold.")
        return v


class PetValidator:

    @staticmethod
    def validate_pet_response(response: Response):
        data = response.text
        try:
            pets = Pets.model_validate_json(data)
            if pets.model_dump()["category"] is None:
                print(pets.model_dump(exclude_unset=True))
                return True
            else:
                print(pets.model_dump())
                return True

        except ValidationError as e:
            print(e.json())
            logger.error(f"Invalid data format {e.json()}")



# try:
#     pets = Pets.model_validate_json(data)
#     if pets.model_dump()["category"] is None:
#         print(pets.model_dump(exclude_unset=True))
#     else:
#         print(pets.model_dump())
#
# except ValidationError as e:
#     print("Error")
#     print(e.json())

# "https://hello.com",
# "https://world.ru"
