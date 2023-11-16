from pydantic import ValidationError
from pages.pet_page_denis.pet_page_denis import PetPage
from src.logger.logger import get_logs
from src.utils.assertions import Assertion
from data.status_code import StatusCode
import allure

# @pysnooper.snoop()
logger = get_logs(r"tests\test_denis\test_pets\test_create_pets.py")


@allure.epic("Testing Create The Pets")
class TestCreateStore:
    assertions = Assertion()
    status_code = StatusCode()
    pet_page = PetPage()

    def test_create_pets(self):
        data = self.pet_page.create_pet_with_data()
        response = self.pet_page.create_pet_with_given_data(data=data)
        self.assertions.assert_status_code(response, self.status_code.STATUS_OK)
