from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Room, Topic


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')

def create_room(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'base/room_form.html', context)

def showRoom(request, pk):
    # room = get_object_or_404(Room, id=pk)
    room = Room.objects.get(id=pk)
    context = {'room': room}
    view_template = 'base/show_room.html'
    return render(request, view_template, context)
