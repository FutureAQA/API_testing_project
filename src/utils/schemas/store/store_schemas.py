import re
from enum import Enum
from typing import Optional
from pydantic import BaseModel, field_validator
from src.logger.logger import get_logs

logger = get_logs("utils/schemas/store/store_schemas")


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
            logger.error("id must be an integer", v)
            raise ValueError("id must be an integer")
        elif v < 0:
            logger.error("id must be greater than 0", v)
            raise ValueError("id must be greater than 0")
        return v

    @field_validator('shipDate')
    @classmethod
    def validate_time_format(cls, value):
        pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}'
        if not re.fullmatch(pattern, value):
            logger.error(f"Неверный формат времени {value}")
            raise ValueError("Неверный формат времени")
        return value
