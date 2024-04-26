from django.contrib import admin

from testing_info.models import Answer_user


@admin.register(Answer_user)
class Answer_userAdmin(admin.ModelAdmin):
    pass