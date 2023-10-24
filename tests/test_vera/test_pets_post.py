"""Test cases for validating pets data and API responses using the POST method."""

import os

import pytest
import requests
import allure
from pprint import pprint

from tests.test_vera.data.status_codes import StatusCode
from src.utils.assertions import Assertion
from tests.test_vera.data.urls import PetUrls
from tests.test_vera.data.data_pets import get_pet_by_status, expected_non_exist_pet_keys, expected_pet_keys
from src.utils.http_methods import MyRequests
from tests.test_vera.conf import pet_data, schema, headers
from tests.test_vera.generator.generator import pet


@allure.epic("POST: Add a new pet to the store")
class TestPostAddPet:
    status_code = StatusCode()
    url = PetUrls
    assertions = Assertion()

    @allure.title("Add a new pet > status code 200")
    def test_add_pet_to_store_has_status_code_200(self, schema):
        """The test checks status code is 200 for the created pet
        :param pet_id
        :return: status code OK 200 """
        schema['id'] = pet['pet_id']
        response = MyRequests.post(
            self.url.PET,
            data=schema
        )
        self.assertions.assert_status_code(response, self.status_code.OK)

    @allure.title("Add a new pet > Response is in json format")
    def test_add_pet_response_is_json_format(self, headers, schema):
        """
        The test checks response is in json format for the created pet
        :param schema, headers
        :return: response is in json format
        """
        response = MyRequests.post(
            self.url.PET,
            data=schema,
            headers=headers
        )
        self.assertions.assert_response_has_be_json(response)

    @allure.title("Add a new pet > Expected pet keys in response")
    def test_add_pet_keys_in_response(self, headers, pet_data):
        """
        The test checks pet keys in json response for the created pet
        :param pet_data
        :return: pet keys in response
        """
        response = MyRequests.post(
            self.url.PET,
            data=pet_data,
            headers=headers
        )
        self.assertions.assert_json_has_keys(response, expected_pet_keys)

    @allure.title("Add a new pet > Expected pet name in response")
    def test_add_pet_name_in_response(self, headers, pet_data):
        """
        The test checks pet's name in json response for the created pet
        :param pet_data
        :return: pet's name in response
        """
        response = MyRequests.post(
            self.url.PET,
            data=pet_data,
            headers=headers
        )
        self.assertions.assert_json_value_by_name(response, "name", pet_data["name"],
                                                  "Incorrect pet name in the response")

    @allure.title("Create pet > Expected pet 'ID' in response")
    def test_add_pet_id_in_response(self, headers, pet_data):
        """
        The test checks "ID" in json response for the created pet
        :param pet_data
        :return: valid pet id in response
        """
        pet_data['id'] = pet["pet_id"]
        response = MyRequests.post(
            self.url.PET,
            pet_data,
            headers=headers)
        actual_pet_id = int(response.json()["id"])
        self.assertions.assert_json_value_by_name(response, "id", actual_pet_id,
                                                  "Incorrect pet id in the response")

    @allure.title("Create pet > Expected pet values in response")
    def test_add_pet_id_in_response(self, headers, pet_data):
        """
        The test checks values in json response for the created pet
        :param pet_data
        :return: valid pet values in response
        """
        pet_data['id'] = pet["pet_id"]
        response = MyRequests.post(
            self.url.PET,
            pet_data,
            headers=headers)
        for key, expected_value in pet_data.items():
            actual_value = response.json().get(key)
            if isinstance(actual_value, int) and isinstance(expected_value, str):
                expected_value = int(expected_value)
            self.assertions.assert_json_value_by_name(response, key, expected_value,
                                                      f"Incorrect pet {expected_value} in the response")
