from django.db import models
from common.models import CommonModel


class Feed(CommonModel):
    title = models.CharField(max_length=120)  # 제목
    content = models.TextField()  # 내용

    # user를 지우면 => 게시글도 지우겠다.
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    # user를 지워도 게시글은 지우지 않겠다
    # user = models.ForeignKey("users.User", on_delete=models.SET_NULL)


# USER
# FEED
# REVIEW

# USER - FEED
# USER -> FEED1. FEED2 유저는 여러개의 게시글 작성 가능
# FEED -> USER1, USER2 게시글은 하나의 유저만
# 1(USER):N(FEED) => 부모: 유저, 자녀: 게시글(FK)
