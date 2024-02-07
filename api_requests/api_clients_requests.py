import random

import requests

URL = 'https://simple-books-api.glitch.me'


# metoda ajutatoare pentru orders API
def get_token():
    random_number_1 = random.randint(1, 999999)
    random_number_2 = random.randint(1, 999999)
    data = {
        "clientName": "Postman",
        "clientEmail": f"test{random_number_1}{random_number_2}@example.com"
    }
    response = requests.post(f'{URL}/api-clients', json=data)
    return response.json()['accessToken']


def create_user(client_name, client_email):
    data = {
        "clientName": client_name,
        "clientEmail": client_email
    }
    response = requests.post(f'{URL}/api-clients', json=data)
    return response
