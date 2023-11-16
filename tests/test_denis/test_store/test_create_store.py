from pages.store_page_denis.store_page_denis import StorePage
from src.utils.assertions import Assertion
from data.status_code import StatusCode
import allure


# @pysnooper.snoop()

@allure.epic("Testing Create a Store")
class TestCreateStore:
    store_page = StorePage()
    assertions = Assertion()
    status_code = StatusCode()

    @allure.title("Create store with valid data has status code 200")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_store_with_valid_data_has_status_code_200(self):
        """
        This test checks if response has status code 200
        """
        data = self.store_page.prepare_store_data()
        response = self.store_page.create_store_with_given_data(data=data)
        self.assertions.assert_status_code(response, self.status_code.STATUS_OK)

    @allure.title("Create store response is JSON")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_store_response_is_json(self):
        """
        This test checks if response is JSON
        """
        data = self.store_page.prepare_store_data()
        response = self.store_page.create_store_with_given_data(data=data)
        self.assertions.assert_response_has_be_json(response)
