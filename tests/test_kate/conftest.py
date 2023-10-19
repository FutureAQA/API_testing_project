import pytest
import requests
import json


@pytest.fixture(scope='function')
def file_read(file):
    f = open(file, 'r', encoding='utf-8')
    j = json.load(f)
    return j