
class Links:

    SERVER_URL = 'https://8e22401d-5c4c-46b3-a692-cc7f7be3ae9b.serverhub.praktikum-services.ru/'

    GET_ORDER_ENDPOINT = 'api/v1/orders/track'
    CREATE_ORDER_ENDPOINT = 'api/v1/orders'
    CANCEl_ORDER_ENDPOINT = 'api/v1/orders/cancel'
    GET_ORDER_FULL_URL = ''.join([SERVER_URL, GET_ORDER_ENDPOINT])

    CREATE_COURIER_ENDPOINT = 'api/v1/courier'
    CREATE_COURIER_FULL_URL = ''.join([SERVER_URL, CREATE_COURIER_ENDPOINT])


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
