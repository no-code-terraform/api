import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

import account.manager


class User(AbstractUser):
    class Meta:
        db_table = 'tfmaker_user'

    username = None
    date_joined = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = account.manager.User()

    password = models.CharField(
        max_length=128,
        editable=False,
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
        null=False,
    )
    last_login = models.DateTimeField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.email
