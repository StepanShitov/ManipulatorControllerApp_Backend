from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import StreamingHttpResponse
from manipulator.camera import VideoCamera, gen

import manipulator

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('Stevie/main_menu/move/', views.move, name='move'),
    path('enter/', views.enter, name='LoginAndPasswordCheck'),
    path('<username>/main_menu/', views.main_menu, name='main_menu'),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')),
]