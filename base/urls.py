from django.urls import path
from django.shortcuts import render, get_object_or_404, redirect
from . import views
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'frontend/index.html')

def go_back(request):
    if 'HTTP_REFERER' in request.META:
        # Redirect to the previous page
        print("################################################################")
        print("HTTP_REFER : " + request.META['HTTP_REFERER'])
        print("################################################################")
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        print("################################################################")
        print("DEFAULT_PAGE_URL")
        print("################################################################")
        # If there's no previous page, redirect to a default page
        return HttpResponseRedirect('default_page_url')

urlpatterns = [
    
    path('', views.home, name="home"),
    path('go-back/', go_back, name='go_back'),

    path('create-room/', views.createRoom, name="create-room"),
    path('room/', views.listRoom, name="list-room"),
    path('room/<str:pk>/', views.showRoom, name="show-room"),
    path('edit-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
]