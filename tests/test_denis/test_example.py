import requests


def test_example():
    url = "https://send-request.me/api/users/?limit=3&offset=0"
    response = requests.get(url)
    print(response.json())