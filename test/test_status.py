from api_requests.status_requests import *


class TestStatusApi:

    def test_status_api_result_status_code(self):
        status_code = get_api_status_code()
        assert status_code == 200, f'Status code should be 200, instead of {status_code}'

    def test_status_api_body(self):
        body = get_api_status_body()
        # body['status']
        assert body.get('status') == 'OK'
        