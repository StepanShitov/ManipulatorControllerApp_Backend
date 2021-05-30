from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import StreamingHttpResponse
from manipulator.camera import VideoCamera, gen

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('<username>/main_menu/', views.main_menu, name='main_menu'),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')),
]