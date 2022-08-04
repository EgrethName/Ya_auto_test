import pytest
import requests

from data import Links


class TestForOrderTracking:

    def test_get_order_by_existing_track_number(self, get_track_number, server_address):
        track_number = {'t': str(get_track_number)}
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params=track_number)
        assert response.status_code == 200

    def test_get_order_by_not_existing_track_number(self, get_track_number, server_address):
        track_number = {'t': str(get_track_number - 1)}
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params=track_number)
        assert response.status_code == 404

    def test_get_order_by_invalid_track_number(self, server_address):
        track_number = {'t': '100jkl'}
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params=track_number)
        assert response.status_code == 404

    def test_get_order_without_track_number(self, server_address):
        response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]))
        assert response.status_code == 400

    def test_get_cancelled_order(self, get_track_number, server_address):
        track_number = {'track': str(get_track_number)}
        response = requests.put(''.join([server_address, Links.CANCEl_ORDER_ENDPOINT]), params=track_number)
        if response.status_code == 200:
            response = requests.get(''.join([server_address, Links.GET_ORDER_ENDPOINT]), params={'t': str(get_track_number)})
            assert response.status_code == 404
        else:
            pytest.xfail("Order cancel is failed")

