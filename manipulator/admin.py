from manipulator.models import User, Logs
from django.contrib import admin


class ShowUsers(admin.ModelAdmin):
    # fields = ['username', 'userPassword']
    list_display = ('username', 'userPassword')


class ShowActions(admin.ModelAdmin):
    list_display = ('actionDate', 'userName', 'actionContains')

admin.site.register(User, ShowUsers)
admin.site.register(Logs, ShowActions)