import allure

from pages.base_page import BasePage
from src.logger.logger import get_logs


logger = get_logs(r"pages\store_page_denis\store_page_denis.py")


class StorePage(BasePage):
    @allure.step("Create store with given data")
    def create_store_with_given_data(self, data):
        """
        This method creates a store with given data and validates response
        :param data:
        :return: response
        """
        url = self.urls.STORES_URL
        response = self.request.post(url=url, data=data)
        return self.validate_response_store(response=response)

