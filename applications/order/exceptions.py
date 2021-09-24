from rest_framework.exceptions import APIException


class OrderDoesNotExistException(APIException):
    status_code = 500
    default_detail = 'Такого заказа не существует.'


class OrderBadStatusException(APIException):
    status_code = 500
    default_detail = 'Заказ в неверном статусе.'
