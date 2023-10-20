"""Test cases for validating pets data and API responses using the GET method."""
import pytest
import requests
import allure
from pprint import pprint

from tests.test_vera.data.status_codes import StatusCode
from tests.test_vera.data.urls import PetUrls
from tests.test_vera.data.data_pets import get_pet_by_status, expected_non_exist_pet_keys, expected_pet_error_msg
from src.utils.http_methods import MyRequests
from tests.test_vera.conf import pet_data, headers
from tests.test_vera.generator.generator import pet


@allure.epic("Test GET method for pets")
class TestGetPet:
    status_code = StatusCode()
    url = PetUrls

    @allure.title("Get pet by status > status code 200")
    @pytest.mark.parametrize("status", get_pet_by_status)
    def test_get_pet_by_status_has_status_code_200(self, status):
        """
        This test checks availability of pets by status and checks the status code of the response
        :param for status: "available", "pending",  "sold"
        :return: status code OK 200
        """
        url = self.url.BY_STATUS
        response = MyRequests().get(
            self.url.BY_STATUS,
            status
        )
        assert response.status_code == self.status_code.OK, f"Unexpected status code."

    @allure.title("Get pet by status > response is JSON format")
    @pytest.mark.parametrize("status", get_pet_by_status)
    def test_get_pet_by_status_response_is_json_type(self, status):
        """
        The test checks if the response content type is JSON
        :param for status: "available", "pending",  "sold"
        :return: JSON format
        """
        response = MyRequests.get(
            self.url.BY_STATUS,
            data=status
        )
        print(response.json())
        assert 'application/json' in response.headers.get('Content-Type', ''), \
            "Error: Response is not in JSON format"

    @allure.title("Get pet by invalid status > status code 400")
    def test_get_pet_by_invalid_status_has_status_code_is_400(self):
        """
        The test checks if the response status code is 400
        :param for status: "invalid_status"
        :return: status code is BAD_REQUEST 400 """
        data = {
            "status": "invalid_status"
        }
        response = MyRequests.get(
            self.url.BY_STATUS,
            data=data
        )
        assert response.status_code == self.status_code.BAD_REQUEST, f"Unexpected status code."

    @allure.title("Get pet by invalid status > Not Found error message")
    def test_get_pet_by_invalid_status_has_error_message(self):
        """
        The test checks if the response error message is "Not Found"
        :param for status: "invalid_status"
        :return:  'message': 'HTTP 404 Not Found' """
        data = {
            "status": "invalid_status"
        }
        response = MyRequests.get(
            self.url.BY_STATUS,
            data=data
        )
        assert response.json().get("message") == expected_pet_error_msg["400 message"], "Wrong error message"

    @allure.title("Get pet by ID > valid ID > status code is 200")
    def test_get_pet_by_id_has_status_code(self, pet_data):
        """
        This test to get pet info by ID and ensure status code is 200
        :param pet_data: pet data
        :return: status code OK 200
        """
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

    @allure.title("Get pet by ID > non existing ID > status code is 404")
    def test_get_pet_by_non_existing_id_status_code_404(self):
        """
        This test to get pet info by non-existing ID and ensure status code is 404
        :param: invalid pet_id = -1
        :return: status code NOT FOUND 404
        """
        pet_id = -1
        response = MyRequests.get(
            self.url.PET + f"/{pet_id}",
        )
        assert response.status_code == self.status_code.NOT_FOUND, \
            f"Unexpected status code. Expected: {self.status_code.NOT_FOUND}, Actual: {response.status_code}"

    @allure.title("Get pet by ID > non existing ID > error messages is 'Pet not found'")
    def test_get_pet_by_non_existing_id_error_message(self):
        """
        This test validates error message in the response for retrieving pet information by non-existing ID
        :param : invalid pet_id = -1
        :return: test for error message
        """
        pet_id = -1
        response = MyRequests.get(
            self.url.PET + f"/{pet_id}",
        )
        assert response.text == expected_pet_error_msg["not found"], "Wrong error message"

    @allure.title("Get pet by ID > deleted pet > status code is 404")
    def test_get_pet_by_id_after_deleting_status_code_404(self, pet_data):
        """
        This test to get pet info by ID and ensure status code is 404 after deleting the pet
        :param pet_data: pets data
        :return: status code NOT FOUND 404
        """
        pet_data["pet_id"] = pet['pet_id']
        # Creating a pet
        response = MyRequests.post(
            self.url.PET,
            data=pet_data
        )
        # Deleting the pet and checking the status code is 200
        actual_pet_id = int(response.json()["id"])
        response = MyRequests.delete(
            self.url.PET + f"/{actual_pet_id}",
            data=pet_data
        )
        assert response.status_code == self.status_code.OK, f"Unexpected status code."
        # Getting status code for the response on attempt to get pet by id
        response = MyRequests.get(
            self.url.PET + f"/{actual_pet_id}",
        )
        assert response.status_code == self.status_code.NOT_FOUND, \
            f"Unexpected status code. Expected: {self.status_code.NOT_FOUND}, Actual: {response.status_code}"

    @allure.title("Get pet by ID > deleted pet > Pet not found error message")
    def test_get_pet_by_id_after_deleting_text(self, pet_data):
        """
        This test to get pet info by ID and ensure "Pet not found" error message after deleting the pet
        :param:  pet_data
        :return: "Pet not found"
        """
        pet_data["pet_id"] = pet['pet_id']
        # Creating a pet
        response = MyRequests.post(
            self.url.PET,
            data=pet_data
        )
        # Deleting the pet and checking the status code is 200
        actual_pet_id = int(response.json()["id"])
        response = MyRequests.delete(
            self.url.PET + f"/{actual_pet_id}",
            data=pet_data
        )
        assert response.status_code == self.status_code.OK, f"Unexpected status code."
        # Getting status code for the response on attempt to get pet by id
        response = MyRequests.get(
            self.url.PET + f"/{actual_pet_id}",
        )
        assert response.text == expected_pet_error_msg["not found"], \
            f"Unexpected response text. Expected: Pet not found, Actual: {response.text}"
