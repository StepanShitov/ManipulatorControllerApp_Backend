from manipulator.models import User
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse
from manipulator.camera import VideoCamera, gen


def index(request):
    return HttpResponse("Hello, world. You're at dead page.")


def login(request):
    return render(request, 'manipulator/authorisation.html')


def main_menu(request, username):
    return render(request, 'manipulator/main_menu.html', {'username' : username})

def checkIfUserExists(login, password):
    usersQuery = User.objects.all()
    for i in usersQuery:
        if i.username == login and i.userPassword == password:
            return True
    return False        

def enter(request):
    if request.method == "POST":
        login = request.POST.get("UserLoginInput", None)
        password = request.POST.get("UserPasswordInput", None)
        if len(login) == 0 or len(password) == 0:
            return render(request, 'manipulator/authorisation.html', {
            'error_message': "Неверный логин или пароль!" })
        if checkIfUserExists(login, password) == False:
            return render(request, 'manipulator/authorisation.html', {
            'error_message': "Пользователь не существует!" })
    return redirect(reverse('main_menu', args=(login, )))
