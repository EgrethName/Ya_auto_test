import pytest
import requests

from data import Links, Payloads


def pytest_addoption(parser):   #  парсер аргументов из консоли
    parser.addoption("--server_address", action="store")


@pytest.fixture(scope="session")
def server_address(request):
    address = request.config.getoption("--server_address")
    if not address:
        pytest.exit('Не передан адрес сервера')
    return address


@pytest.fixture(scope='class')
def get_track_number(server_address):
    response = requests.post(''.join([server_address, Links.CREATE_ORDER_ENDPOINT]), json=Payloads.PAYLOAD_FOR_ORDER)
    response_json = response.json()
    track_number = response_json['track']
    yield track_number
    track_request = {'track': str(track_number)}
    requests.put(''.join([server_address, Links.CANCEl_ORDER_ENDPOINT]), params=track_request)


@pytest.fixture(scope='session')
def delete_courier(server_address):
    yield
    for i in range(1, 50):
        requests.delete(''.join([server_address, Links.DELETE_COURIER_ENDPOINT, str(i)]))
