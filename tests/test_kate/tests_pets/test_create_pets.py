import allure
from pages.pet_page_denis.pet_page_denis import PetPage
from data.data_kate.data_kate import AllData
import pytest
import json
from data.status_code import StatusCode
from src.utils.assertions import Assertion


@allure.epic("Test create pet")
class TestCreatePets:
    pet_page = PetPage()
    status_code = StatusCode()
    assertions = Assertion()

    @allure.title("test_create_pets_check_response_value_without_required_key")
    @pytest.mark.parametrize('key', AllData.PETS_REQUIRED_KEYS)
    def test_create_pets_check_response_value_without_required_key(self, key):
        """
        This test checks the correct values for 'msg' and 'type' in response
        when creating a pet with a missing required key.
        :param key: The required key that will be missing in the request.
        """
        data = self.pet_page.prepare_pet_data(key=key)
        response = self.pet_page.create_pet_with_given_data(data=data)
        response_json_list = json.loads(response)
        for response_dict in response_json_list:
            assert response_dict['msg'] == 'Field required'
            assert response_dict['type'] == 'missing'

    @allure.title("test_create_pets_check_response_status_code_without_optional_key")
    @pytest.mark.parametrize('key', AllData.PET_OPTIONAL_KEYS)
    def test_create_pets_check_response_status_code_without_optional_key(self, key):
        """
        Verifies that the response returns a status code 200 when creating a pet
        with a missing optional key.
        :param key: The optional key that will be missing in the request.
        """
        data = self.pet_page.prepare_pet_data(key=key)
        response = self.pet_page.create_pet_with_given_data(data=data)
        self.assertions.assert_status_code(response, self.status_code.STATUS_OK)
