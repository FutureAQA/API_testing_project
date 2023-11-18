"""
This file contains a class TestCreateStore with tests for checking the creation of a pet
"""

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

    @allure.title("Create pets with valid data has status code 200")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_pets_with_valid_data_has_status_code_200(self):
        """
        This test checks if response has status code 200 after creating pets
        """
        data = self.pet_page.prepare_pet_data()
        response = self.pet_page.create_pet_with_given_data(data=data)
        self.assertions.assert_status_code(response, self.status_code.STATUS_OK)
