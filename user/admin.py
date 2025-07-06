from django.contrib import admin
from user.models import CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    pass
