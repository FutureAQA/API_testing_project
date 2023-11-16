from src.logger.logger import get_logs
from src.utils.assertions import Assertion
from src.utils.http_methods import MyRequests

logger = get_logs("tests/test_denis/test_example")


class TestGetPets:
    assertions = Assertion()
    request = MyRequests()

    def test_example(self):
        import requests

        url = "https://indonesia-latest-weather-and-earthquake.p.rapidapi.com/feelbylocal_top15_earthquake"

        headers = {
            "X-RapidAPI-Key": "7b963c3402msh55aa1b07ce9e0c8p134ed4jsne1af87f84354",
            "X-RapidAPI-Host": "indonesia-latest-weather-and-earthquake.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        print(response.json())
