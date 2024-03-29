"""
This module contains PetValidator class and its methods
"""

from pydantic import ValidationError
from requests import Response

from src.logger.logger import get_logs
from src.utils.schemas.pets.pets_schemas import Pets

logger = get_logs(r"src\utils\schemas\pets\pet_validator")


class PetValidator:
    @staticmethod
    def validate_pet_response(response: Response):
        """
        This method validates that the response matches the expected schema
        :param response: response
        :return: True if the response matches the expected schema, otherwise returns error message
        """
        data = response.text
        try:
            pets = Pets.model_validate_json(data)
            if pets.model_dump()["category"] is None:
                pets.model_dump(exclude_unset=True)
                return True
            else:
                pets.model_dump()
                return True

        except ValidationError as e:
            logger.error(f"Invalid data format {e.json()}")
            return e.json()
