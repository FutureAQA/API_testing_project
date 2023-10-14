import string
import random


data_user = [
    {
        'id': 3434,
        'username': 'Garry44545',
        'firstName': 'Garry4',
        'lastName': 'Garry4',
        'email': 'rt@we',
        'password': '123'
    }
]
username = data_user[0]['username']


def generate_random_string(length=9):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
