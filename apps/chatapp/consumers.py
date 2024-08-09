import json
from channels.generic.websocket import WebsocketConsumer



class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        # return super().connect()
        super().connect()
        
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected.'
        }))
    
    
    def receive(self, text_data=None, bytes_data=None):
        # Handle incoming WebSocket data
        text_data_json = json.loads(text_data) 
        
        # Send a response back to the WebSocket
        self.send(text_data=json.dumps({
            'type': 'message',
            'message': text_data_json
        }))
    
    
    def send(self, text_data=None, bytes_data=None, close=False):
        return super().send(text_data, bytes_data, close)