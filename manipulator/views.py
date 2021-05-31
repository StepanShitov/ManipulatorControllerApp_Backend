from manipulator.models import User
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse
from manipulator.camera import VideoCamera, gen
from manipulator.sendToArduino import *



def index(request):
    return HttpResponse("Hello, world. You're at dead page.")


def login(request):
    return render(request, 'manipulator/authorisation.html')


def main_menu(request, username):
    if(request.POST.get('forward')):
        print("1")
    if(request.POST.get('left')):
        print("2")
    if(request.POST.get('take')):
        print("3")
    if(request.POST.get('right')):
        print("4")
    if(request.POST.get('back')):
        print("5")
    if(request.POST.get('mcrprBtn')):
        print("6")
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

def request_page(request):
    if(request.POST.get('mybtn')):
        print("1")