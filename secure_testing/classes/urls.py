from django.urls import path
from .views import create_class

urlpatterns = [
    path("create/", create_class, name="create_class"),
]
