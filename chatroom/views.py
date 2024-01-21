from django.shortcuts import render, redirect
from .models import chat
# Create your views here.
def index(request):
    if request.method == 'POST':
        room_name = request.POST['room']
        get_room = chat.objects.filter(room_name = room_name)
        if get_room:
            c = get_room[0]
            number = c.allowed_user
            if int(number) < 2:
                return redirect(f'{room_name}/join')
        else:
            create = chat.objects.create(room_name = room_name, allowed_user = 1)
            if create:
                return redirect(f'{room_name}/created')
    return render(request, 'index.html')

def stream(request, room_name, created):
    return render(request, 'stream.html', {'room' : room_name, 'created':created})
