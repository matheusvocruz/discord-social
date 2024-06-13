import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from handler.send_message_handler import SendMessageHandler

intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    sendMessageHandler: SendMessageHandler = SendMessageHandler(message)

    if message.author == client.user:
        return 
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')

    await sendMessageHandler.handler()

def main () -> None:
    load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config/.env'))
    client.run(token=os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    main()