from manipulator.models import User
from django.contrib import admin


class ShowUsers(admin.ModelAdmin):
    # fields = ['username', 'userPassword']
    list_display = ('username', 'userPassword')

admin.site.register(User, ShowUsers)