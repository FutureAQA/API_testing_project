"""
This module contains the StoreValidator class and its methods
"""

from pydantic import ValidationError
from requests import Response

from src.logger.logger import get_logs
from src.utils.schemas.store.store_schemas import Store

logger = get_logs(r"src\utils\schemas\store\store_validator.py")


class StoreValidator(Store):
    @staticmethod
    def validate_store_response(response: Response):
        """
        This method validates that the response matches the expected schema
        :param response: response
        :return: True if the response matches the expected schema, otherwise returns error message
        """
        data = response.text
        try:
            store = Store.model_validate_json(data)
            if store.model_dump()["shipDate"] is None:
                store.model_dump(exclude_unset=True)
                return True
            else:
                store.model_dump()
                return True

        except ValidationError as e:
            logger.error(f"Invalid data format {e.json()}")
            return e.json()
