import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'global_notifications'

        # Join global notifications group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from room group
    async def send_notification(self, event):
        message = event['message']
        event_type = event.get('event_type', 'info')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'event_type': event_type
        }))
