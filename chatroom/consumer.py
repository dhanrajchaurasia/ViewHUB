from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class StreamConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print('connected....')
        await  self.accept()
        
        


    async def receive(self, text_data):
        content = json.loads(text_data)
        print('mssg recieved from client',content['command'])

        if(content['command'] == 'join_room'):
            
            await self.channel_layer.group_add(content['room'], self.channel_name)
            print('joindd')

        elif(content['command'] == 'join'):
            await self.channel_layer.group_send(content['room'], {
                'type':'join.message'
            })

        elif(content['command'] == 'offer'):
            await self.channel_layer.group_send(content['room'], {
                'type':'offer.message',
                'offer':content['offer']
            })

        elif(content['command'] == 'answer'):
            await self.channel_layer.group_send(content['room'],{
                'type':'answer.message',
                'answer':content['answer']
            })
        elif(content['command'] == 'send_msg'):
            await self.channel_layer.group_send(content['room'],{
                'type':'sendMsg.message',
                'msg':content['text'],
                'sender': content['sender']
            })

        elif(content['command'] == 'candidate'):
            await self.channel_layer.group_send(content['room'],{
                'type':'candidate.message',
                'candidate': content['candidate'],
                'iscreated': content['iscreated']
            })

    async def join_message(self, event):
        await self.send_json({
            'command':'join'
        })

    async def offer_message(self, event):
        await self.send_json({
            'command': 'offer',
            'offer': event['offer'] 
        })

    async def answer_message(self, event):
        await self.send_json({
            'command': 'answer',
            'answer': event['answer']
        })

    async def candidate_message(self, event):
        await self.send_json({
            'command': 'candidate',
            'candidate': event['candidate'],
            'iscreated': event['iscreated']
        })

    async def sendMsg_message(self, event):
        print(event)
        await self.send(json.dumps({
            'command':'send_msg',
            'text':event['msg'],
            'sender':event['sender'],
        }))
                              
    
    async def disconnect(self, event):
        print('disconnected...')
        pass