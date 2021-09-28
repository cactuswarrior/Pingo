from asyncio.windows_events import NULL
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
from accounts.models import Accounts
from .models import Words,Ranking,Room,UserInRoom
from channels.db import database_sync_to_async

def get_users():
    users = Accounts.objects.all()
    for _ in users:
        continue
    return users

def create_user():
    now = datetime.datetime.now()
    print(now)
    return Accounts.objects.create(user_name="kim", time_to_expire=now)

def update_room(room_num):
    room = Room.objects.get(room_id = room_num)
    room.is_started = True
    room.save()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = 'game_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("socket created")
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        # await database_sync_to_async(create_user)()
<<<<<<< HEAD
        # users = await database_sync_to_async(get_users)()
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("text_data:", text_data_json)
        flag = text_data_json['type']
        if flag == 'chat':
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        elif flag == 'game':
            await database_sync_to_async(update_room)(self.scope['url_route']['kwargs']['room_name'])
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'game_message'
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        print("event:", event)
=======
        users = await database_sync_to_async(get_users)()
        print(users)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print("46:", text_data_json)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print("59:", event)
>>>>>>> 72d8a620c4ae0ac780b83e1f5b188a2f15be1922
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def game_message(self, event):
        print("event:", event)
        await self.send(text_data=json.dumps({
            'message': "game started"
        }))

# class GameConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'game_%s' % self.room_name
#
#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#     # Receive message from WebSocket
#     async def receive(self):
#         # await database_sync_to_async(create_user)()
#
#         room = Room.objects.get()
#         room.is_started = True
#         room.save()
#
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'start_messsage',
#                 'message': "game_started"
#             }
#         )
#
#     # Receive message from room group
#     async def start_message(self, event):
#         message = event['message']
#         print(event)
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))