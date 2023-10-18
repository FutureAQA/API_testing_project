from pages.store_page_denis.store_page_denis import StorePage
from src.utils.assertions import Assertion
from data.status_code import StatusCode
import allure
# @pysnooper.snoop()

@allure.epic("Testing Store")
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
        response = self.store_page.create_store_with_valid_data()
        self.assertions.assert_status_code(response, self.status_code.STATUS_OK)

