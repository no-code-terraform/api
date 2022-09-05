from django.http import HttpRequest, JsonResponse

from tfmaker.helper import http
from .domain import constant, context


def index(
    request: HttpRequest
) -> JsonResponse:
    return http \
        .response_json_200({
            'name': constant.APP_NAME,
            'description': constant.APP_DESCRIPTION,
            'licence': constant.APP_LICENSE,
        })


def services(
    request: HttpRequest
) -> JsonResponse:
    services = context.service_storage().findall()
    return http \
        .response_json_200({
            'services': [vars(i) for i in services]
        })
