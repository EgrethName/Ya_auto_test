import pytest
import requests

from data import Links


class TestForCreateCourier:

    def test_check_for_login(self, expected_status_code):
        response = requests.post(Links.CREATE_COURIER_FULL_URL, json=courier_data)
        assert response.status_code == expected_status_code
