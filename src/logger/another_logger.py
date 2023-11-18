"""
This module contains a class for logging requests and responses
"""


import datetime
import os
from requests import Response
from pages.folder_management import FolderManagement


class Logger:
    folder_management = FolderManagement()
    file_name = f"""log_{str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}.log"""
    project_dir = folder_management.get_root_path()
    log_dir = os.path.join(project_dir, "logs")

    log_file = os.path.join(log_dir, file_name)

    @classmethod
    def _write_log_to_file(cls, data: str):
        """
        This method writes data to the log file
        :param data: data
        """
        with open(cls.log_file, "a", encoding="utf-8") as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        """
        This method adds request to the log
        :param url: url of the request
        :param data: data of the request
        :param headers: headers of the request
        :param cookies: cookies of the request
        :param method: method of the request
        """
        test_name = os.environ.get("PYTEST_CURRENT_TEST")

        data_to_add = f"\n{'-' * 100}\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request url: {url}\n"
        data_to_add += f"Request data: {data}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"Request cookies: {cookies}\n"
        data_to_add += f"\n"

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        """
        This method adds response to the log
        :param response: response
        """
        cookies = dict(response.cookies)
        headers = dict(response.headers)

        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response.text}\n"
        data_to_add += f"Response headers: {headers}\n"
        data_to_add += f"Response cookies: {cookies}\n"
        data_to_add += f"\n{'-' * 100}\n"

        cls._write_log_to_file(data_to_add)
