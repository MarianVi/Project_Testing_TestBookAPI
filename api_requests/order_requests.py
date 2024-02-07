import requests

from api_requests import api_clients_requests

URL = 'https://simple-books-api.glitch.me'

token = api_clients_requests.get_token()
headers = {
    'Authorization': token
}


def submit_order(book_id, customer_name):
    data = {
        "bookId": book_id,
        "customerName": customer_name
    }
    response = requests.post(f'{URL}/orders', json=data, headers=headers)
    return response


def submit_order_custom_keys():
    data = {
        "bookId": 1,
        "costomerName": 'Test'
    }
    response = requests.post(f'{URL}/orders', json=data, headers=headers)
    return response


def get_all_orders():
    response = requests.get(f'{URL}/orders', headers=headers)
    return response


def get_order(order_id):
    response = requests.get(f'{URL}/orders/{order_id}', headers=headers)
    return response


def update_an_order(order_id, new_customer_name):
    data = {
        'customerName': new_customer_name
    }
    response = requests.patch(f'{URL}/orders/{order_id}', json=data, headers=headers)
    return response


def delete_an_order(order_id):
    response = requests.delete(f'{URL}/orders/{order_id}', headers=headers)
    return response

# print(submit_order(1, 'John').json())
# submit_order(1, 'John')
# submit_order(3, 'Andrew')
# submit_order(4, 'Mark')
#
# for order in get_all_orders():
#     print(order)
#
# order_id = submit_order(3,'Ana').json()['orderId']
# print(order_id)
# print(get_order(order_id).json())

# update order
# facem o comanda
# order = submit_order(5, 'Vlad').json()
#
# # facem request de get_order la comanda facuta mai sus
# print(get_order(order['orderId']).json())
#
# # facem update la comanda facuta mai sus, schimbam customer name
# response = update_an_order(order['orderId'], 'John')
#
# # afisam status code-ul (204)
# print(response.status_code)
#
# # facem din nou request de get_order, ca sa verificam modificarea customer name
# print(get_order(order['orderId']).json())
#
# # arunca eroare deoarece request-ul de update nu returneaza niciun body
# print(response.json())
#
# order_id = submit_order(4, 'John').json()['orderId']
# print(get_order(order_id).json())
# print(delete_an_order(order_id).status_code)
# print(get_order(order_id).json())
