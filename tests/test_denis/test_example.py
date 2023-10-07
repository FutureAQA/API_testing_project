import requests


def test_example():
    url = "https://serverest.dev/login"
    data = {
      "email": "fulano@qa.com",
      "password": "teste"
}
    response = requests.post(url, json=data)
    print(response.json())