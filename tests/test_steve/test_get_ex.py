import requests

url='https://petstore.swagger.io/v2/'

def test_get_find_by_status():
    path='pet/findByStatus?status=available'
    response=requests.get(url+path)
    print(response.json())