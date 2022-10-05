import uuid

from django.db import models
from django_jsonform.models.fields import JSONField

from api.domain import (
    config,
    constant,
)


class Service(models.Model):
    class Meta:
        db_table = 'tfmaker_service'

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
    )
    provider = models.CharField(
        max_length=50,
        choices=(
            (constant.PROVIDER_AWS, 'Awmazon Web Service'),
            (constant.PROVIDER_GCP, 'Google Cloud Platform'),
            (constant.PROVIDER_SCW, 'Scaleway Cloud'),
        )
    )
    type = models.CharField(
        max_length=25,
        choices=(
            (constant.SERVICE_TYPE_COMPUTE, 'Compute'),
            (constant.SERVICE_TYPE_DATABASE, 'Database'),
            (constant.SERVICE_TYPE_STORAGE, 'Storage'),
        )
    )
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    url = models.URLField()
    tf_key = models.CharField(
        max_length=50,
        unique=True,
        default=None,
    )
    extra = JSONField(
        schema={
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                    },
                    'type': {
                        'type': 'string',
                        'choices': config.SERVICE_EXTRA_TYPES,
                    },
                    'min': {
                        'type': 'interger',
                        'required': False,
                        'default': None,
                    },
                    'max': {
                        'type': 'interger',
                        'required': False,
                        'default': None,
                    },
                    'choices': {
                        'type': 'list',
                        'items': {
                            'type': 'string',
                        },
                        'default': None,
                        'required': False,
                    },
                    'is_multiple_choice': {
                        'type': 'boolean',
                        'default': False,
                        'required': False,
                    },
                    'default': {
                        'type': 'string',
                        'required': False,
                    },
                },
            }
        },
        default=list,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name
