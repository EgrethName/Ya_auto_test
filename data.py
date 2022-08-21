

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


