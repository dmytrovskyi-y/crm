from django.contrib import admin

from .models import UserModel


class UsersAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserModel, UsersAdmin)
