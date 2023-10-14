"""Test cases for validating pets data and API responses using the GET method."""
import pytest
import requests
from pprint import pprint

from tests.test_vera.data.status_codes import StatusCode
from tests.test_vera.data.urls import PetUrls
from tests.test_vera.data.data_pets import get_pet_by_status, expected_non_exist_pet_keys
from src.utils.http_methods import MyRequests
from tests.test_vera.conf import pet_data


class TestGetPet:
    status_code = StatusCode()
    url = PetUrls

    @pytest.mark.parametrize("status", get_pet_by_status)
    def test_get_pet_by_status_has_status_code_200(self, status):
        """
        This test checks availability of pets by status and checks the status code of the response
        :param for status: "available", "pending",  "sold"
        """
        url = self.url.BY_STATUS
        response = MyRequests().get(
            self.url.BY_STATUS,
            status
        )
        assert response.status_code == self.status_code.OK, f"Unexpected status code."

    @pytest.mark.parametrize("status", get_pet_by_status)
    def test_get_pet_by_status_response_is_json_type(self, status):
        """ The test checks if the response content type is JSON """
        response = MyRequests.get(
            self.url.BY_STATUS,
            data=status
        )
        print(response.json())
        assert 'application/json' in response.headers.get('Content-Type', ''), \
            "Error: Response is not in JSON format"

    def test_get_pet_by_invalid_status(self):
        """ The test checks if the response content type is JSON """
        data = {
            "status": "invalid_status"
        }
        response = MyRequests.get(
            self.url.BY_STATUS,
            data=data
        )
        assert response.status_code == self.status_code.OK, f"Unexpected status code."
        assert response.json() == []

    def test_get_pet_by_id_status_code(self, pet_data):
        """This test to get pet info by ID and ensures status code is 200"""
        # creating a pet
        response = MyRequests.post(
            self.url.PET,
            data=pet_data,
        )
        pet_id = response.json()['id']
        # getting status code for the response
        response = MyRequests.get(
            self.url.PET + f"/{pet_id}",
        )
        pprint(response.json())
        assert response.status_code == self.status_code.OK, f"Unexpected status code."

    def test_get_pet_by_non_existing_id_status_code_404(self):
        """This test to get pet info by non-existing ID and ensures status code is 404"""
        pet_id = -1
        response = MyRequests.get(
            self.url.PET + f"/{pet_id}",
        )
        assert response.status_code == self.status_code.NOT_FOUND, \
            f"Unexpected status code. Expected: {self.status_code.NOT_FOUND}, Actual: {response.status_code}"

    @pytest.mark.parametrize("name, expected_value, error_message", expected_non_exist_pet_keys)
    def test_get_pet_by_non_existing_id_error_message(self, name, expected_value, error_message):
        """
        This test validates error message in the response for retrieving pet information by non-existing ID
        """
        pet_id = -1
        response = MyRequests.get(
            self.url.PET + f"/{pet_id}",
        )
        assert name in response.json(), f"""response JSON doesn't have key '{name}'"""
        assert response.json()[name] == expected_value, error_message
