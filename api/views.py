import json
import os
import shutil
import tempfile

from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
)

from api.domain import (
    constant,
    context,
)
from api.domain.usecase import build_tf as uc_build_tf
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


def build_tf(
    request: HttpRequest
) -> HttpResponse:
    if request.method != 'POST':
        return http.response_json_405()

    try:
        tf_data = json.loads(request.body)
    except:
        return http.response_json_400(
            message='Invalid json data')

    with tempfile.TemporaryDirectory() as tf_path:
        uc_build_tf.execute(tf_data=tf_data, tf_path=tf_path)
        zip_tf_path = shutil.make_archive(
            base_name=tf_path,
            format='zip',
            root_dir=tf_path,
        )

        content = open(zip_tf_path, 'rb').read()
        os.remove(zip_tf_path)

        return HttpResponse(
            content,
            content_type='application/zip',
            headers={
                'Content-Disposition': f'attachment; filename=tf.zip'
            }
        )
