import requests


def test_example():
    url = "https://serverest.dev/login"
    data = {
      "email": "denisbacchus@qa.com",
      "password": "qwerty123456zxcvb"
}
    response = requests.post(url, json=data)
    print(response.json())