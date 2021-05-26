from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'chat/login.html',)

def room(requests, room_name):
    requests.encoding='utf-8'
    if 'user' in requests.GET and requests.GET['user']:
        return render(requests, 'chat/room.html', {
            'room_name': room_name,
            'user_name': requests.GET["user"],
        })