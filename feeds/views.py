from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT

# views.py
# -> serializer를 불러오고, 클라이언트에서 데이터를 받거나 전달하는 역할을 한다


# api/v1/feeds GET(조회) POST(생성)
# api/v1/feeds/id GET(조회) DELETE(삭제) PUT(업데이트)
from .models import Feed
from .serializers import FeedSerializer


class AllFeed(APIView):
    def get(self, request):
        feeds = Feed.objects.all()

        # object -> json
        serializer = FeedSerializer(feeds, many=True)  # 게시글은 여러개이기에 안 해주면 오류남)
        return Response(serializer.data)

    # 데이터 저장
    def post(self, request):
        # { "title":"게시글 생성"} => JSON
        serializer = FeedSerializer(data=request.data)  # 유저가 보낸 데이터(JSON)

        if serializer.is_valid():
            # feed = serializer.save(user=request.user)
            serializer.save(user=request.user)
            return Response("success")
        else:
            return Response(serializer.errors)


# api/v1/feeds/id, get put delete 해보기. api 만들기를 많이 해봐야 한다.
class FeedDetail(APIView):
    def get(self, request, feed_id):
        pass

    def put(self, request, feed_id):
        pass

    def delete(self, request, feed_id):
        pass
