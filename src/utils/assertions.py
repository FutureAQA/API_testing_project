import json
from requests import Response


class Assertion:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code}, Actual: {actual_status_code}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        assert name in response_json, f"""response JSON doesn't have key '{name}'"""

