import pytest
import requests

from data import Links, Payloads


def pytest_addoption(parser):   #  парсер аргументов из консоли
    parser.addoption("--server_address", action="store")


@pytest.fixture(scope="session")
def server_address(request):
    return request.config.getoption("--server_address")


@pytest.fixture(scope='class')
def get_track_number(server_address):
    response = requests.post(''.join([server_address, Links.CREATE_ORDER_ENDPOINT]), json=Payloads.PAYLOAD_FOR_ORDER)
    response_json = response.json()
    track_number = response_json['track']
    return track_number


@pytest.fixture(scope='session')
def delete_courier(server_address):
    yield
    for i in range(1, 50):
        response = requests.delete(''.join([server_address, Links.DELETE_COURIER_ENDPOINT, str(i)]))
    print('All couriers delete from db')

