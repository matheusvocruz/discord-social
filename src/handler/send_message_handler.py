from discord import Message
from model.response import Response

class SendMessageHandler:
    message: Message
    response: Response = Response()

    def __init__(self, message: Message) -> None:
        self.message = message
        pass

    async def handler(self) -> None:
        if not self.message.content or self.message.content[0] == '?':
            return

        try:
            newMessage : str = self.response.get_message(self.message.content)
            
            if newMessage is None: 
                return
            
            await self.delete()
            await self.sendMessage(newMessage)
        except Exception as e:
            print(e)

    async def delete(self) -> None:
        await self.message.delete()

    async def sendMessage(self, newMessage: str) -> None:
        await self.essage.channel.send(f'Re-post <@{self.message.author.id}>: ' + newMessage)