from django.urls import path
from sample_swagger.views import TestView, SerializerView

urlpatterns = [
    path("v1/test/", TestView.as_view(), name="test"),
    path("v1/serializer/", SerializerView.as_view(), name="serializer"),
]
