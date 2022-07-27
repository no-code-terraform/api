from django.contrib import admin
from django.urls import include, path

from api import views

urlpatterns = [
    path('', views.index),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
