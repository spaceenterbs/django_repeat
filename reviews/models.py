from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    content = models.CharField(max_length=150)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)


# USER
# REVIEW

# USER - REVIEW, REVIEW 유저는 여러개의 리뷰 작성가능
# REVIEW -> USER 리뷰는 하나의 유저만 가능
# 1(USER):N(REVIEW) => 부모: 유저, 자녀: 게시글(FK)

# USER
# REVIEW

# FEED - REVIEW, REVIEW 유저는 여러개의 리뷰 작성가능
# FEED -> REVIEW 리뷰는 하나의 유저만 가능
# 1(USER):N(REVIEW) => 부모: 유저, 자녀: 게시글(FK)
