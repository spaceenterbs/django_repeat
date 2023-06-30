from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel


class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)


# from django.db import models

# # Create your models here.
