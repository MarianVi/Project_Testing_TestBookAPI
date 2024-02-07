from api_requests.order_requests import *


class TestOrders:
    def test_status_code_valid_order_request(self):
        response = submit_order(1, 'Marian')
        assert response.status_code == 201
        # clean up
        delete_an_order(response.json()['orderId'])

    def test_created_value(self):
        response = submit_order(3, 'Oana')
        body = response.json()
        assert body['created'] == True
        # clean up
        delete_an_order(response.json()['orderId'])

    def test_delete_order(self):
        order_id = submit_order(3, 'Andrei').json()['orderId']
        response = delete_an_order(order_id)
        assert response.status_code == 204

    def test_get_all_orders_zero_order(self):
        response = get_all_orders()
        assert len(response.json()) == 0

    def test_get_multiple_orders(self):
        order_id_1 = submit_order(1, 'Ion').json()['orderId']
        order_id_2 = submit_order(1, 'Vali').json()['orderId']
        order_id_3 = submit_order(1, 'Sabin').json()['orderId']
        response = get_all_orders()
        assert len(response.json()) == 3
        # clean up
        delete_an_order(order_id_1)
        delete_an_order(order_id_2)
        delete_an_order(order_id_3)

    def test_get_order(self):
        order_id = submit_order(4, 'Laur').json()['orderId']
        response = get_order(order_id)
        body = response.json()
        assert body['id'] == order_id
        assert body['bookId'] == 4
        assert body['customerName'] == 'Laur'
        # clean up
        delete_an_order(order_id)

    def test_update_order(self):
        order_id = submit_order(3, 'Cristian').json()['orderId']
        response = update_an_order(order_id, 'Marian')
        assert response.status_code == 204
        response_get_order = get_order(order_id)
        assert response_get_order.json()['customerName'] == 'Marian'
        # clean up
        delete_an_order(response)

    def test_submit_order_bad_request(self):
        response = submit_order_custom_keys()
        # clean up
        delete_an_order(response.json()['orderId'])
        assert response.status_code == 400

    def test_submit_a_book_order_out_of_stock(self):
        response = submit_order(2, 'John')
        assert response.status_code == 404
        assert response.json()['error'] == 'This book is not in stock. Try again later.'

    def test_submit_a_book_order_with_invalid_id(self):
        response = submit_order(9, 'Marian')
        assert response.status_code == 400
        assert response.json()['error'] == 'Invalid or missing bookId.'


