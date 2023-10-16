from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ValidationError, field_validator


class GetComplete(Enum):
    true = True
    false = False


class GetStatus(Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"


class Store(BaseModel):
    id: Optional[int] = 0
    petId: Optional[int] = 0
    quantity: Optional[int] = 0
    shipDate: Optional[str] = None
    status: GetStatus
    complete: GetComplete

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
        # pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z'
        # if not re.fullmatch(pattern, value):
        #     raise ValueError("Неверный формат времени")
        try:
            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            raise ValueError("Неверный формат времени")
        return value


data = """{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2023-10-15T13:27:05.244Z",
  "status": "delivered",
  "complete": true
}"""

try:
    store = Store.model_validate_json(data)
    if store.model_dump()["shipDate"] is None:
        print(store.model_dump(exclude_unset=True))
    else:
        print(store.model_dump())

except ValidationError as e:
    print("Error")
    print(e.json())
