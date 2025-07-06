from django.contrib import admin

from manager.models import Feedback


@admin.register(Feedback)
class AdminFeedback(admin.ModelAdmin):
    search_fields = ["name", ]
