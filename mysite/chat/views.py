from django.shortcuts import render
from .models import Group,Message
# Create your views here.
def index(request):
    return render(request, '../templates/chat.html')


def room(request, room_name):
    return render(request, '../templates/room.html', {
        'room_name': room_name
    })
