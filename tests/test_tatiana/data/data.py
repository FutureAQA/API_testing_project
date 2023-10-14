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
data_user_put = {
        'id': 3434,
        'username': 'Wendy5656',
        'firstName': 'Wendy5656',
        'lastName': 'Wendy5656',
        'email': 'Wendy5656@we',
        'password': '12345'
    }
username = data_user[0]['username']
username_put = data_user_put['username']

def generate_random_string(length=9):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
