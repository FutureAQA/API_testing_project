from pydantic import ValidationError
from requests import Response

from src.logger.logger import get_logs
from src.utils.schemas.pets.pets_schemas import Pets

logger = get_logs(r"src\utils\schemas\pets\pet_validator")


class PetValidator:
    @staticmethod
    def validate_pet_response(response: Response):
        data = response.text
        try:
            pets = Pets.model_validate_json(data)
            if pets.model_dump()["category"] is None:
                print(f"1 {pets.model_dump(exclude_unset=True)}")
                return True
            else:
                print(f"2 {pets.model_dump()}")
                return True

        except ValidationError as e:
            logger.error(f"Invalid data format {e.json()}")
            print(f"Invalid data format {e.json()}")
            return e.json()
