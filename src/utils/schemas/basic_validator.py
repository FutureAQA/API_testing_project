"""
This module contains the BasicValidator class and its methods
"""

import re

import allure


class BasicValidator:
    @allure.description("Verify that the email is valid")
    def is_valid_email(self, email):
        """
        :param email: given email
        :return: True if the email is valid, False otherwise
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email)

    @allure.description("Verify that the status is valid")
    def is_valid_status(self, status):
        """
        :param status: given status
        :return: True if the status is valid, False otherwise
        """
        valid_statuses = ["available", "pending", "sold"]
        return status in valid_statuses
