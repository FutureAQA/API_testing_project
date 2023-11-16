import allure

from pages.base_page import BasePage
from src.logger.logger import get_logs

logger = get_logs(r"pages\pet_page_denis\pet_page_denis.py")


class PetPage(BasePage):

    @allure.step("Create pet with given data")
    def create_pet_with_given_data(self, data):
        """
        This method creates a pet with given data and validates response
        :param data:
        :return: response
        """
        url = self.urls.PET_URL
        response = self.request.post(url=url, data=data)
        return self.validate_response_pet(response=response)
