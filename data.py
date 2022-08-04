import random


def generate_random_string(string_length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_string = ''.join(random.choice(letters) for i in range(string_length))
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


class CourierLoginData:

    SUCCESSFUL_LOGIN = {
        "login": "courier",
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_2 = {
        "login": "fr",
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_1 = {
        "login": "f",
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_3 = {
        "login": "fro",
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_9 = {
        "login": "frodobagg",
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_10 = {
        "login": "frodobaggi",
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_11 = {
        "login": "frodobaggin",
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_255 = {
        "login": generate_random_string(255),
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_LENGTH_256 = {
        "login": generate_random_string(256),
        "password": "1234",
        "firstName": "frodo"
    }
    CYRILLIC_LOGIN = {
        "login": "фродо",
        "password": "1234",
        "firstName": "frodo"
    }
    SPEC_SYMBOLS_LOGIN = {
        "login": "!№;%:\"",
        "password": "1234",
        "firstName": "frodo"
    }
    DIGITAL_STR_LOGIN = {
        "login": "56789",
        "password": "1234",
        "firstName": "frodo"
    }
    DIGITAL_INT_LOGIN = {
        "login": 56789,
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_NONE = {
        "login": None,
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_TRUE = {
        "login": True,
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_FALSE = {
        "login": False,
        "password": "1234",
        "firstName": "frodo"
    }
    LOGIN_WITH_SPACES = {
        "login": "   ",
        "password": "1234",
        "firstName": "frodo"
    }



