import random

from api_requests.api_clients_requests import create_user


class TestAuth:
    def test_auth_with_correct_values_status_code(self):
        random_number_1 = random.randint(1, 999999)
        body = {
            'clientName': 'Postman_test',
            'clientEmail': f'ftest{random_number_1}@example.com'
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 201

    def test_auth_with_correct_values_response_token(self):
        random_number_1 = random.randint(1, 999999)
        body = {
            'clientName': 'Postman_test',
            'clientEmail': f'test{random_number_1}@example.com'
        }
        response = create_user(body['clientName'], body['clientEmail'])
        response_body = response.json()
        assert 'accessToken' in response_body.keys()

    def test_invalid_format_email(self):
        body = {
            'clientName': 'Postman_test',
            'clientEmail': 'example.com'
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 400
        assert response.json()['error'] == 'Invalid or missing client email.'

    def test_auth_without_client_email(self):
        body = {
            'clientName': 'Postmanfan',
            'clientEmail': ''
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 400
        assert response.json()['error'] == 'Invalid or missing client email.'

    def test_auth_without_client_name(self):
        body = {
            'clientName': '',
            'clientEmail': 'test123@example.com'
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 400
        assert response.json()['error'] == 'Invalid or missing client name.'

    def test_auth_with_same_email(self):
        random_number_1 = random.randint(1, 999999)
        body = {
            'clientName': 'Postman_test',
            'clientEmail': f'test{random_number_1}@example.com'
        }
        create_user(body['clientName'], body['clientEmail'])
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 409
        assert response.json()['error'] == 'API client already registered. Try a different email.'
