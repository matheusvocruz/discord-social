import os
from dotenv import load_dotenv
from service.discord_bot import DiscordBot

def main () -> None:
    load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config/.env'))

    discord_bot: DiscordBot = DiscordBot(token=os.getenv('DISCORD_TOKEN'))
    discord_bot.run()

if __name__ == '__main__':
    main()