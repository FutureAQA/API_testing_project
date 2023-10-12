"""Test cases for validating pets data and API responses using the GET method."""

import pytest
import requests

from tests.test_vera.data.status_codes import StatusCode
from tests.test_vera.data.urls import PetUrls
from tests.test_vera.data.data_pets import get_pet_by_status
from src.utils.http_methods import MyRequests


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
