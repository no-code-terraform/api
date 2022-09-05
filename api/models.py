import uuid

from django.db import models

from api.domain import constant


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
    extra = models.JSONField(
        default=dict,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name
