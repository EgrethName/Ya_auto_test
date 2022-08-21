import pytest
import random
import requests

from data import Links


def generate_random_string(string_length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return random_string


def create_login_data(login):
    login_data = {
        "login": login,
        "password": "1234",
        "firstName": "frodo"
    }
    return login_data


class TestForCreateCourier:

    test_data = [
        pytest.param(create_login_data(generate_random_string(7)), 201, id="test_successful_courier_create"),
        pytest.param(create_login_data(generate_random_string(2)), 201, id="test_login_length_2"),
        pytest.param(create_login_data(generate_random_string(1)), 400, id="test_login_length_1"),
        pytest.param(create_login_data(generate_random_string(3)), 201, id="test_login_length_3"),
        pytest.param(create_login_data(generate_random_string(9)), 201, id="test_login_length_9"),
        pytest.param(create_login_data(generate_random_string(10)), 201, id="test_login_length_10"),
        pytest.param(create_login_data(generate_random_string(11)), 400, id="test_login_length_11"),
        pytest.param(create_login_data(generate_random_string(255)), 400, id="test_login_length_255"),
        pytest.param(create_login_data(generate_random_string(256)), 400, id="test_login_length_256"),
        pytest.param(create_login_data("фродо"), 400, id="test_cyrillic_login"),
        pytest.param(create_login_data("!№;%:\""), 400, id="test_spec_symbols_login"),
        pytest.param(create_login_data("56789"), 400, id="test_digital_str_login"),
        pytest.param(create_login_data(56789), 400, id="test_digital_int_login"),
        pytest.param(create_login_data(None), 400, id="test_login_none"),
        pytest.param(create_login_data(True), 400, id="test_login_true"),
        pytest.param(create_login_data(False), 400, id="test_login_false"),
        pytest.param(create_login_data("   "), 400, id="test_login_with_spaces")
    ]

    @pytest.mark.parametrize("payload,expected_status_code", test_data)
    def test_check_for_login(self, payload, expected_status_code, server_address, delete_courier):
        response = requests.post(''.join([server_address, Links.CREATE_COURIER_ENDPOINT]), json=payload)
        assert response.status_code == expected_status_code
