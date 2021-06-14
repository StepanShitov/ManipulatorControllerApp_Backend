from manipulator.models import User, Logs
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from manipulator.camera import VideoCamera, gen
from manipulator.sendToArduino import *



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

def move(request):
    username = request.POST['username'].replace('Hello, ', '')
    if request.POST['activity'] == "mcrPr":
        userActivity = request.POST['activity'] + " ---" + request.POST['commands']
    else: 
        userActivity = request.POST['activity']
    dateAndTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    newUserLog = Logs(actionDate=dateAndTime,userName=username,actionContains=userActivity)
    newUserLog.save()

    if request.POST['activity'] == "forward":
        print("button forward is pressed")
        sendData("1")
    elif request.POST['activity'] == "leftRight":
        print("button leftRightTake is pressed")
        sendData("2")
    elif request.POST['activity'] == "back":
        print("button back is pressed")
        sendData("3")
    elif request.POST['activity'] == "mcrPr":
        print("button microcomand perform is pressed")
        sendData("3")
    return HttpResponse('')