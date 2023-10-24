import json
from requests import Response
from src.logger.logger import get_logs


logger = get_logs(r"src\utils\assertions")

class Assertion:

    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            logger.error(f"Unexpected status code. Expected: {expected_status_code}, Actual: {actual_status_code}")

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_json = response.json()
            assert name in response_json, logger.error(f"response JSON doesn't have key {name}")
        except json.JSONDecodeError as e:
            logger.error(e)
            logger.error(f"Response is not JSON format. Response text is {response.text}")

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_json = response.json()
            for name in names:
                assert name in response_json, logger.error(f"response JSON doesn't have key {name}")
        except json.JSONDecodeError as e:
            logger.error(e)
            logger.error(f"Response is not JSON format. Response text is {response.text}")

    @staticmethod
    def assert_response_has_be_json(response: Response):
        try:
            assert 'application/json' in response.headers.get('Content-Type', '')
        except json.JSONDecodeError as e:
            logger.error(e)
            logger.error(f"Error: Response is not in JSON format")

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_json = response.json()
            assert name in response_json, f"""response JSON doesn't have key '{name}'"""
            actual_value = response_json[name]
            assert actual_value == expected_value, error_message
        except json.JSONDecodeError as e:
            logger.error(e)
            logger.error(f"""Response is not JSON format. Response text is '{response.text}'""")

    @staticmethod
    def assert_json_values_by_names(response, expected_data):
        try:
            response = response.json()
            for key, value in expected_data.items():
                assert key in response, f"""Response JSON doesn't have key '{key}'"""
                assert response[key] == value, f"Mismatch for key '{key}' - Expected: {value}, Actual: {response[key]}"
        except json.JSONDecodeError as e:
            logger.error(e)
            logger.error(f"""Response is not JSON format. Response text is '{response.text}'""")

