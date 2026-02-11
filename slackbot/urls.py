from django.urls import path
from .views import gen_tests

urlpatterns = [
    path("gen-tests/", gen_tests),
]