# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     name = models.CharField(
#         max_length=50,
#     )

#     like_posts = models.ManyToManyField(
#         "posts.Post",
#         verbose_name="좋아요 누른 Post 목록",
#         related_name="like_users",
#         blank=True,
#     )

#     def __str__(self):
#         return self.username
