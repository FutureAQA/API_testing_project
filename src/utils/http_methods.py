"""
This module contains methods for sending HTTP requests
"""

import requests
from data.urls import Urls
from src.logger.another_logger import Logger
from src.logger.logger import get_logs

logger = get_logs(r"src\utils\http_methods.py")


class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        """
        Send POST request to given url with given data
        :param url: request url
        :param data: request data
        :param headers: request headers
        :param cookies: request cookies
        :return: response
        """
        return MyRequests._send(url, data, headers, cookies, "POST")

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        """
        Send GET request to given url
        :param url: request url
        :param data: request data
        :param headers: request headers
        :param cookies: request cookies
        :return: response
        """
        return MyRequests._send(url, data, headers, cookies, "GET")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        """
        Send PUT request to given url with given data
        :param url: request url
        :param data: request data
        :param headers: request headers
        :param cookies: request cookies
        :return: response
        """
        return MyRequests._send(url, data, headers, cookies, "PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        """
        Send DELETE request to given url
        :param url: request url
        :param data: request data
        :param headers: request headers
        :param cookies: request cookies
        :return: response
        """
        return MyRequests._send(url, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        """
        Send HTTP request to given url with given data and a specific method
        :param url: request url
        :param data: request data
        :param headers: request headers
        :param cookies: request cookies
        :param method: request method
        :return: response
        """
        url = f"{Urls.BASE_URL}{url}"

        if headers is None:
            headers = {"Content-Type": "application/json"}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, json=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"""Bad method '{method}' was received""")

        Logger.add_response(response)
        logger.info(f"Response data: {data}")

        return response
