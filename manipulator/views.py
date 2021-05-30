from manipulator.models import User
from django.shortcuts import render, resolve_url
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at dead page.")


def login(request):
    return render(request, 'manipulator/authorisation.html')


def main_menu(request, username):
    return render(request, 'manipulator/main_menu.html', {'username' : username})