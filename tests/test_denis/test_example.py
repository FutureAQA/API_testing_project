from src.logger.logger import get_logs
from src.utils.assertions import Assertion
from src.utils.http_methods import MyRequests

logger = get_logs("tests/test_denis/test_example")


class TestGetPets:
    assertions = Assertion()
    request = MyRequests()

    def test_example(self):
        pet_id = 100
        url = f"/pet/{pet_id}"
        response = self.request.get(url=url)
        logger.error(response.json())
        print(response.json())
        # self.assertions.assert_status_code(response, 200)
