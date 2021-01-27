import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Client
from channels.db import database_sync_to_async

class Consumer(AsyncWebsocketConsumer):
    room_group_name = 'default_room'

    async def connect(self):
        print('connect: channel_name={}'.format(self.channel_name))

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print('disconnect: channel_name={}'.format(self.channel_name))
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print('receive')
        text_data_json = json.loads(text_data)
        command = text_data_json['command']

        print('command={}'.format(command))
        if command == 'get_members':
            all_clients = await self.get_all_clients()
            await self.send(text_data=json.dumps({
                'command': 'get_members',
                'members': all_clients
            }))
        elif command == 'connect':
            id = text_data_json['id']

    async def send_joining(self, event):
        print('send_joining')
        id = event['id']
        name = event['name']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'command': 'joining',
            'id': id,
            'name': name
        }))

    async def send_leaving(self, event):
        print('send_leaving')
        id = event['id']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'command': 'leaving',
            'id': id
        }))

    @database_sync_to_async
    def get_all_clients(self):
        print('get_all_clients')
        clients = Client.objects.all()
        clients_data = {}
        for c in clients:
            clients_data[c.id] = {
                'name': c.name
            }
        #clients_data = list(map(lambda x: {'id': x.id, 'name': x.name}, clients))
        return clients_data

