from django.http import JsonResponse
from . import APP_DESCRIPTION, APP_LICENSE, APP_NAME


def index(request) -> JsonResponse:
    return JsonResponse({
        'name': APP_NAME,
        'description': APP_DESCRIPTION,
        'licence': APP_LICENSE,
    })
