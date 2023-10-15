import json
from typing import Optional
import validators

from pydantic import BaseModel, ValidationError, field_validator


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
    id: int
    name: str
    category: Category | CategoryId = None
    photoUrls: Optional[list[str]] = []
    tags: list[Tags | TagsId] = []
    status: str

    @field_validator("photoUrls")
    @classmethod
    def check_photo_urls(cls, v: list[str]) -> list[str]:
        for url in v:
            if not (validators.url(url) or url.startswith("data:image")):
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
  
    "name": "doggie",
        "photoUrls": ["https://hello.com", "https://world.ru"],
    "tags": [
    ],
    "status": "sold"
}
"""

try:
    pets = Pets.model_validate_json(data)
    if "category" not in pets.model_dump():
        print(pets.model_dump_json(exclude_unset=True))
    else:
        print(pets.model_dump_json())

except ValidationError as e:
    print("Error")
    print(e.json())

# "https://hello.com",
# "https://world.ru"


