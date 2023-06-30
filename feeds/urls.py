from django.urls import path
from . import views


# api/v1/feeds GET(조회, 생성)
# api/v1/feeds/id GET(조회, 삭제, 업데이트)

urlpatterns = [path("", views.AllFeed.as_view())]
