from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/index.html',)

def room(requests, room_name):
    return render(requests, 'chat/room.html', {
        'room_name': room_name,
    })