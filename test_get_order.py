import requests

from data import Links, DataGeneration as DataGen


class TestForOrderTracking:

    def test_get_order_by_existing_track_number(self, get_track_number, server_address):
        track_request = {'t': str(get_track_number)}
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params=track_request)
        assert response.status_code == 200

    def test_get_order_by_not_existing_track_number(self, get_track_number, server_address):
        track_request = {'t': str(get_track_number - 1)}
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params=track_request)
        assert response.status_code == 404

    def test_get_order_by_invalid_track_number(self, server_address):
        track_request = {'t': DataGen.generate_rand_str}
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params=track_request)
        assert response.status_code == 404

    def test_get_order_without_track_number(self, server_address):
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]))
        assert response.status_code == 400

    def test_get_cancelled_order(self, get_track_number, server_address):
        track_request = {'track': str(get_track_number)}
        requests.put(''.join([server_address, Links.CANCEl_ORDER_ENDPOINT]), params=track_request)
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params={'t': str(get_track_number)})
        assert response.status_code == 404
