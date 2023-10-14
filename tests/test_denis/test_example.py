import os
import allure
import pytest
import requests
from src.utils.logger.logger import get_logs
from src.utils.http_methods import MyRequests

logger = get_logs("tests/test_denis/test_example")
request = MyRequests()


def test_example():
    url = "/pet/100"
    # response = requests.get(url=url)
    response = request.get(url=url)
    logger.error(response.json())
    print(response.json())
    # assert response.status_code == 404
