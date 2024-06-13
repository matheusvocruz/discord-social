from discord import Intents, Client, Message
from handler.send_message_handler import SendMessageHandler

class DiscordBot(Client):
    __token: str = None

    def __init__(self, token: str) -> None:
        self.__token = token
        super().__init__(intents=self.__build_intents())
        pass

    async def on_ready(self) -> None:
        print(f'DiscordBot is now running!')

    async def on_message(self, message: Message) -> None:
        sendMessageHandler: SendMessageHandler = SendMessageHandler(message)

        if message.author == self.user:
            return 
        
        await sendMessageHandler.handle()

    def run(self) -> None:
        super().run(self.__token)

    def __build_intents(self) -> Intents:
        intents: Intents = Intents.default()
        intents.message_content = True
        return intents