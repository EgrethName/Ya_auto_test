import pytest
import requests
import psycopg2
from data import Links, Payloads


# def connect_to_database():
#     con = psycopg2.connect(
#         database="scooter_rent",
#         user="20e1031b-5f44-4950-b4d6-d9a8b82d91a4",
#         password="smith",
#         host="serverhub.praktikum-services.ru",
#         port="4554"
#     )
#     print("Database opened successfully")

@pytest.fixture(autouse=true)
def setup_url():
    pass


@pytest.fixture(scope='class')
def get_track_number():
    response = requests.post(''.join([Links.SERVER_URL, Links.CREATE_ORDER_ENDPOINT]), json=Payloads.PAYLOAD_FOR_ORDER)
    response_json = response.json()
    track_number = response_json['track']
    return track_number

#
# connect_to_database()
