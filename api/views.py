from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
)

from api.domain import (
    constant,
    context,
)
from tfmaker.helper import http


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


def download(
    request: HttpRequest
) -> HttpResponse:
    return HttpResponse(
        content_type='application/zip',
        headers={
            'Content-Disposition': 'attachment; filename=tf.zip'
        }
    )
