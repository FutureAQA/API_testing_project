"""
This file contains UserPage class and all its methods
"""

import allure
from pages.base_page import BasePage
from src.logger.logger import get_logs

logger = get_logs(r"pages\user_page_denis\user_page_denis.py")


class UserPage(BasePage):

    @allure.step("Create user with the given data")
    def create_user_with_given_data(self, data):
        """
        This method creates a user with given data and validates response
        :param data: data
        :return: response
        """
        url = self.urls.USER_URL
        response = self.request.post(url=url, data=data)
        return self.validate_response_user(response=response)
