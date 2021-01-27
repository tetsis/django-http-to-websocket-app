from django.shortcuts import render, redirect
import uuid
from .models import Client
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.
def join(request):
    print('join')
    if request.method == 'GET':
        id = request.COOKIES.get('id')
        if id is not None:
            print('Redirect to index')
            return redirect('index')

        print('Render join page')
        return render(request, 'roomapp/join.html')
    elif request.method == 'POST':
        name = request.POST['name']
        id = str(uuid.uuid4())

        # Save
        print('Save client: id={}, name={}'.format(id, name))
        client = Client(id=id, name=name)
        client.save()

        # Send message to room group
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'default_room',
            {
                'type': 'send_joining',
                'id': id,
                'name': name
            }
        )

        print('Redirect to main(index) page')
        response = redirect('index')
        response.set_cookie('id', id)
        return response

def leave(request):
    print('leave')
    if request.method == 'POST':
        id = request.COOKIES.get('id')

        # Delete
        print('Delete client: id={}'.format(id))
        Client.objects.filter(id=id).delete()

        # Send message to room group
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'default_room',
            {
                'type': 'send_leaving',
                'id': id
            }
        )

        print('Redirect to join page')
        response = redirect('join')
        response.delete_cookie('id')
        return response

def index(request):
    print('index')
    id = request.COOKIES.get('id')
    if id is None:
        print('Redirect to join page')
        return redirect('join')

    print('Render main(index) page')
    return render(request, 'roomapp/index.html')
