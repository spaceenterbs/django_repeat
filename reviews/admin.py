from django.contrib import admin
from .models import Review


# Register your models here.
@admin.register(Review)
class FeedAdmin(admin.ModelAdmin):
    list_display = ("content", "created", "updated")
