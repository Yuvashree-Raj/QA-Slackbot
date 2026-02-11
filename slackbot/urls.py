from django.urls import path
from .views import slack_generate_testcases

urlpatterns = [
    path("gen-tests/", slack_generate_testcases),
]