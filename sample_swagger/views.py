from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .open_api_params import get_params, post_params
from .serializers import (
    GetRequestSerializer,
    GetResponseSerializer,
    PostRequestSerializer,
    PostResponseSerializer,
)

"""
// request
{
    'param1': integer,
    'param2': string,
    'param3': date,
}

// response
{
    'status': 200,
    'message': 'SUCCESS'
}
"""

"""
//request
{
    "school_name": "KNU",
    "student_list": [
        {
            "first_name": "Hanseul",
            "last_name": "Jo"
        },
        {
            "first_name": "Hanseul",
            "last_name": "Cho"
        }
    ]
}

//response
{
    "status": 201,
    "message": "SUCCESS"
}
"""


class SerializerView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        query_serializer=GetRequestSerializer, response={"200": GetResponseSerializer}
    )  # (manual_parameters=get_params)
    def get(self, request):
        return Response("Swagger 연동 테스트")

    @swagger_auto_schema(
        request_body=PostRequestSerializer, responses={"201": PostResponseSerializer}
    )  # (request_body=post_params)
    def post(self, request):
        return Response("Swagger Schema")


class TestView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(manual_parameters=get_params)
    def get(self, request):
        return Response("Swagger 연동 테스트")

    @swagger_auto_schema(request_body=post_params)
    def post(self, request):
        return Response("Swagger Schema")
