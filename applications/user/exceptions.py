from rest_framework.exceptions import APIException


class PerformerDoesNotExistException(APIException):
    status_code = 500
    default_detail = 'Такого исполнителя не существует.'
