import requests
from requests import Response
from data.data_kate.data_kate import AllData


class Assertion:

    def assert_status_code(self, response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            f'Unexpected status_code. Expected_status_code:{expected_status_code}, Actual:{actual_status_code}.'

    def assert_text(self, actual_text: str, expected_text: str):
        assert actual_text == expected_text, 'Wrong text'

    def assert_response_is_json(self, response: Response):
        assert 'application/json' in response.headers.get('Content-Type', ''), 'Response is not in JSON format'

    def assert_check_message(self, response: Response, person_info):
        assert response.json()['message'] == str(person_info['id']), 'Message in response is not correct'

    def assert_dicts_values_matches(self, user_data, person_info):
        for key in person_info:
            assert str(user_data[key]) == str(person_info[key]), f"Key value is not correct for key: {key}"

    def assert_keys_in_response(self, item_list, keys_to_check):
        for item in item_list:
            self.assert_user_keys_in_response(item, keys_to_check)

    def assert_keys_in_dict(self, user_data: dict, keys_to_check: list):
        for key in keys_to_check:
            assert key in user_data, f"Key '{key}' is missing in the response"

    def assert_check_updated_values(self, updated_data, expected_data):
        for key in expected_data:
            assert str(updated_data[key]) == str(expected_data[key]), f"Key value is not correct for key: {key}"



