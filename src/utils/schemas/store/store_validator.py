from pydantic import ValidationError
from requests import Response

from src.logger.logger import get_logs
from src.utils.schemas.store.store_schemas import Store

logger = get_logs(r"src\utils\schemas\store\store_validator")


class StoreValidator(Store):
    @staticmethod
    def validate_store_response(response: Response):
        data = response.text
        try:
            store = Store.model_validate_json(data)
            if store.model_dump()["shipDate"] is None:
                store.model_dump(exclude_unset=True)
            else:
                store.model_dump()

        except ValidationError as e:
            logger.error(f"Invalid date format {e.json()}")
