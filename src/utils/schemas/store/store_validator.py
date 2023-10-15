from datetime import datetime
from typing import Optional
import validators
import re
from pydantic import BaseModel, ValidationError, field_validator


class Store(BaseModel):
    id: Optional[int] = 0
    petId: Optional[int] = 0
    quantity: Optional[int] = 0
    shipDate: str = None
    status: str
    complete: bool

    @field_validator("id", "petId", "quantity")
    @classmethod
    def check_int(cls, v: int):
        if not isinstance(v, int):
            raise ValueError("id must be an integer")
        elif v < 0:
            raise ValueError("id must be greater than 0")
        return v

    @field_validator('shipDate')
    @classmethod
    def validate_time_format(cls, value):
        pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z'
        if not re.fullmatch(pattern, value):
            raise ValueError("Неверный формат времени")
        try:
            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            raise ValueError("Неверный формат времени")

        return value


data = """{
  
  "petId": 0,
  "quantity": 0,
  
  "status": "placed1",
  "complete": true
}"""

try:
    pets = Store.model_validate_json(data)
    print(pets.model_dump_json())

except ValidationError as e:
    print("Error")
    print(e.json())
