import pytest
import requests

from data import Links, DataGeneration as DataGen


class TestForCreateCourier:

    test_data = [
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(7)), 201, id="test_successful_courier_create"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(2)), 201, id="test_login_length_2"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(1)), 400, id="test_login_length_1"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(3)), 201, id="test_login_length_3"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(9)), 201, id="test_login_length_9"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(10)), 201, id="test_login_length_10"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(11)), 400, id="test_login_length_11"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(255)), 400, id="test_login_length_255"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_str(256)), 400, id="test_login_length_256"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_non_ascii_str(7)), 400, id="test_cyrillic_login"),
        pytest.param(DataGen.create_login_data(DataGen.generate_specsymb_str(7)), 400, id="test_spec_symbols_login"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_digit_str(7)), 400, id="test_digital_str_login"),
        pytest.param(DataGen.create_login_data(DataGen.generate_rand_digit()), 400, id="test_digital_int_login"),
        pytest.param(DataGen.create_login_data(None), 400, id="test_login_none"),
        pytest.param(DataGen.create_login_data(True), 400, id="test_login_true"),
        pytest.param(DataGen.create_login_data(False), 400, id="test_login_false"),
        pytest.param(DataGen.create_login_data("   "), 400, id="test_login_with_spaces")
    ]

    @pytest.mark.parametrize("payload,expected_status_code", test_data)
    def test_check_for_login(self, payload, expected_status_code, server_address, delete_courier):
        response = requests.post(''.join([server_address, Links.CREATE_COURIER_ENDPOINT]), json=payload)
        assert response.status_code == expected_status_code
