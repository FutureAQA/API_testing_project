from typing import Optional
from pydantic import BaseModel, ValidationError, field_validator

from src.logger.logger import get_logs
from src.utils.schemas.basic_validator import BasicValidator


logger = get_logs(r"utils\schemas\users\user_schemas.py")

validator = BasicValidator()


class User(BaseModel):
    id: Optional[int] = 10
    username: Optional[str] = "theUser"
    firstName: Optional[str] = "John"
    lastName: Optional[str] = "James"
    email: Optional[str] = "john@email.com"
    password: Optional[str] = "12345"
    phone: Optional[str] = "12345"
    userStatus: Optional[int] = 1

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if not validator.is_valid_email(v):
            raise ValueError("Invalid email address")
        return v

