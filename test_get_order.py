import pytest
import requests

from data import Links


class TestForOrderTracking:

    # test_cases = [
    #     pytest.param(TrackNumber.EXISTING_TRACK_NUMBER, 200, id='test_get_order_by_existing_track_number'),
    #     pytest.param(TrackNumber.NOT_EXISTING_TRACK_NUMBER, 404, id='test_get_order_by_not_existing_track_number'),
    #     pytest.param(TrackNumber.INVALID_TRACK_NUMBER, 404, id='test_get_order_by_invalid_track_number'),
    #     pytest.param(TrackNumber.MISSING_TRACK_NUMBER, 400, id='test_get_order_without_track_number'),
    #     pytest.param(TrackNumber.EXISTING_TRACK_NUMBER, 404, id='test_get_cancelled_order'),
    # ]
    #
    # @pytest.mark.parametrize("track_number, expected_status_code", test_cases)
    # def test_request(self, track_number, expected_status_code):
    #     response = requests.get(Links.GET_ORDER_FULL_URL, json=track_number)
    #     assert response.status_code == expected_status_code

    def test_get_order_by_existing_track_number(self, get_track_number):
        track_number = {'t': str(get_track_number)}
        print(track_number)
        response = requests.get(Links.GET_ORDER_FULL_URL, params=track_number)
        assert response.status_code == 200

    def test_get_order_by_not_existing_track_number(self, get_track_number):
        track_number = {'t': str(get_track_number - 1)}
        response = requests.get(Links.GET_ORDER_FULL_URL, params=track_number)
        assert response.status_code == 404

    def test_get_order_by_invalid_track_number(self):
        track_number = {'t': '100jkl'}
        response = requests.get(Links.GET_ORDER_FULL_URL, params=track_number)
        assert response.status_code == 404

    def test_get_order_without_track_number(self):
        response = requests.get(Links.GET_ORDER_FULL_URL)
        assert response.status_code == 400

    def test_get_cancelled_order(self, get_track_number):
        track_number = {'track': str(get_track_number)}
        response = requests.put(''.join([Links.SERVER_URL, Links.CANCEl_ORDER_ENDPOINT]), params=track_number)
        if response.status_code == 200:
            response = requests.get(Links.GET_ORDER_FULL_URL, params={'t': str(get_track_number)})
            assert response.status_code == 404
        else:
            pytest.xfail("Order cancel is failed")

