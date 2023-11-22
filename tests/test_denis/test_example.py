from pprint import pprint

import pytest
import requests

from data.status_code import StatusCode
from pages.pet_page_denis.pet_page_denis import PetPage
from pages.store_page_denis.store_page_denis import StorePage
from src.logger.logger import get_logs
from src.utils.assertions import Assertion
from src.utils.http_methods import MyRequests

logger = get_logs("tests/test_denis/test_example")


class TestGetPets:
    store_page = StorePage()
    pet_page = PetPage()
    assertions = Assertion()
    status_code = StatusCode()

    def test_example(self):
        dct = self.pet_page.prepare_tags()
        print()
        print(dct)
        data = self.pet_page.add_field_in_the_body(dct)
        print()
        print(data)

    # @pytest.mark.parametrize("item", ['dfhdfh', True, "122411", ["sdgsd"], {"hello": "world"}])
    # @pytest.mark.parametrize("item", ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'])
    def test_example1(self):
        url = "https://petstore3.swagger.io/api/v3/store/order/"
        dict_data = self.store_page.prepare_store_data(ship_date="sdgsdgsd")
        print()
        print(dict_data)
        response = requests.post(url=url, json=dict_data)
        print(response.json())
        print(response.status_code)

    def test_example2(self):
        url = "https://petstore3.swagger.io/api/v3/pet/"
        dict_data = self.pet_page.prepare_pet_data()
        print()
        pprint(dict_data)
        data = self.pet_page.add_field_in_the_body(dict_data)
        print()
        pprint(data)
        # response = requests.post(url=url, json=data)
        # print(response.json())
        # print(response.status_code)

    def test_example3(self):
        url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
        response = requests.get(url)
        # for i in response.json():
        #     print(i)
        print(response.json()[4])