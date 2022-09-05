from django.contrib import admin

from api import models

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'provider',
        'type',
        'created_at',
    ]
    list_filter = [
        'provider',
        'type',
    ]
    readonly_fields = [
        'id',
        'created_at',
    ]


admin.site.register(models.Service, ServiceAdmin)
