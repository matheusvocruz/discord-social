from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CHANNEL: Final[str] = os.getenv('CHANNEL')

intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    # empty or private message
    if not user_message or user_message[0] == '?':
        return

    try:
        response: str = get_response(user_message)
        
        if response is None:
            return
        
        await message.delete()
        
        channel = client.get_channel(int(CHANNEL))
        await channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')

    if (message.channel.id != int(CHANNEL)):
        return

    await send_message(message, user_message)

def main () -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()