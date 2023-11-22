"""
This file contains a class TestCreateUser with test methods for checking the creation of a user
"""
import allure

from data.status_code import StatusCode
from pages.user_page_denis.user_page_denis import UserPage
from src.utils.assertions import Assertion


@allure.epic("Testing Create a User")
class TestCreateUser:
    user_page = UserPage()
    assertions = Assertion()
    status_code = StatusCode()

    @allure.title("Create user with valid data has status code 200")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_with_valid_data_has_status_code_200(self):
        """
        This test checks if response has status code 200
        """
        data = self.user_page.prepare_user_data()
        response = self.user_page.create_user_with_given_data(data=data)
        self.assertions.assert_status_code(response, self.status_code.STATUS_OK)
