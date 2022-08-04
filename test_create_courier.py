import pytest
import requests

from data import Links, CourierLoginData


class TestForCreateCourier:

    test_data = [
        pytest.param(CourierLoginData.SUCCESSFUL_LOGIN, 201, id="test_successful_courier_create"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_2, 201, id="test_login_length_2"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_1, 400, id="test_login_length_1"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_3, 201, id="test_login_length_3"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_9, 201, id="test_login_length_9"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_10, 201, id="test_login_length_10"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_11, 400, id="test_login_length_11"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_255, 400, id="test_login_length_255"),
        pytest.param(CourierLoginData.LOGIN_LENGTH_256, 400, id="test_login_length_256"),
        pytest.param(CourierLoginData.CYRILLIC_LOGIN, 400, id="test_cyrillic_login"),
        pytest.param(CourierLoginData.SPEC_SYMBOLS_LOGIN, 400, id="test_spec_symbols_login"),
        pytest.param(CourierLoginData.DIGITAL_STR_LOGIN, 400, id="test_digital_str_login"),
        pytest.param(CourierLoginData.DIGITAL_INT_LOGIN, 400, id="test_digital_int_login"),
        pytest.param(CourierLoginData.LOGIN_NONE, 400, id="test_login_none"),
        pytest.param(CourierLoginData.LOGIN_TRUE, 400, id="test_login_true"),
        pytest.param(CourierLoginData.LOGIN_WITH_SPACES, 400, id="test_login_with_spaces")
    ]

    @pytest.mark.parametrize("payload,expected_status_code", test_data)
    def test_check_for_login(self, payload, expected_status_code, server_address, delete_courier):
        response = requests.post(''.join([server_address, Links.CREATE_COURIER_ENDPOINT]), json=payload)
        assert response.status_code == expected_status_code
