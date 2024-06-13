from discord import Message
from model.response import Response

class SendMessageHandler:
    __message: Message
    __response: Response = Response()

    def __init__(self, message: Message) -> None:
        self.__message = message
        pass

    async def handle(self) -> None:
        if not self.__message.content or self.__message.content[0] == '?':
            return

        try:
            new_message : str = self.__response.get_message(self.__message.content)
            
            if new_message is None: 
                return
            
            await self.__delete()
            await self.__send_message(new_message)
        except Exception as e:
            print(e)

    async def __delete(self) -> None:
        await self.__message.delete()

    async def __send_message(self, new_message: str) -> None:
        await self.__message.channel.send(self.__build_message(self.__message.author.id, new_message))

    def __build_message(self, author: str, message: str) -> str:
        return f'Re-post <@{author}>: ' + message