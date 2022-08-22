import random
import string


class DataGeneration:

    @staticmethod
    def create_login_data(login):
        login_data = {
            "login": login,
            "password": "1234",
            "firstName": "frodo"
        }
        return login_data

    @staticmethod
    def generate_rand_str(string_length):
        letters_eng = string.ascii_lowercase
        random_string = ''.join(random.choice(letters_eng) for i in range(string_length))
        return random_string

    @staticmethod
    def generate_rand_non_ascii_str(string_length):
        letters_rus = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
        random_string = ''.join(random.choice(letters_rus) for i in range(string_length))
        return random_string

    @staticmethod
    def generate_rand_digit_str(string_length):
        letters_digit = string.digits
        random_string = ''.join(random.choice(letters_digit) for i in range(string_length))
        return random_string

    @staticmethod
    def generate_rand_digit():
        random_number = random.randint(100000, 999999)
        return random_number

    @staticmethod
    def generate_specsymb_str(string_length):
        letters_specsymbols = string.digits
        random_string = ''.join(random.choice(letters_specsymbols) for i in range(string_length))
        return random_string


class Links:

    GET_ORDER_ENDPOINT = 'api/v1/orders/track'
    CREATE_ORDER_ENDPOINT = 'api/v1/orders'
    CANCEl_ORDER_ENDPOINT = 'api/v1/orders/cancel'

    CREATE_COURIER_ENDPOINT = 'api/v1/courier'
    DELETE_COURIER_ENDPOINT = 'api/v1/courier/'


class Payloads:

    PAYLOAD_FOR_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
