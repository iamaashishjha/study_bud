from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Room, Topic

from .forms import RoomForm

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'frontend/index.html', context)

def listRoom(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'frontend/base/room_list.html',context)

def showRoom(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    view_template = 'frontend/base/room_show.html'
    return render(request, view_template, context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        print("################################################################")
        print("Deleted Room")
        print("################################################################")
        print(request.META['HTTP_REFERER'])
        print("################################################################")
        return redirect('home')
    context = {'obj': room}
    return render(request, 'base/delete.html', context)
