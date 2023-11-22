"""
This module contains the UserValidator class and its methods
"""

from pydantic import ValidationError
from requests import Response

from src.logger.logger import get_logs
from src.utils.schemas.users.user_schemas import User

logger = get_logs(r"src\utils\schemas\store\store_validator.py")


class UserValidator(User):

    @staticmethod
    def validate_user_response(response: Response):
        """
        This method validates that the response matches the expected schema
        :param response: response
        :return: True if the response matches the expected schema, otherwise returns error message
        """
        data = response.text
        try:
            user = User.model_validate_json(data)
            if user.model_dump():
                return True
        except ValidationError as e:
            logger.error(f"Invalid data format {e.json()}")
            return e.json()
