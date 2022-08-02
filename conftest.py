import pytest
import requests
from data import Links, Payloads


@pytest.fixture(scope='class')  # создание заказа перед выполнением тестов
def get_track_number():
    response = requests.post(''.join([Links.SERVER_URL, Links.CREATE_ORDER_ENDPOINT]), json=Payloads.PAYLOAD_FOR_ORDER)
    response_json = response.json()
    track_number = response_json['track']
    return track_number
#
#
# @pytest.fixture(scope='class')
# def cancel_order():
#     track_number = {'track': get_track_number}
#     response = requests.put(''.join([Links.SERVER_URL, Links.CANCEl_ORDER_ENDPOINT]), json=track_number)
#     if response.status_code == 200:
#         return True
#     else:
#         return False
