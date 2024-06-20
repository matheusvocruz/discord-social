from service.discord_bot import DiscordBot
from util.settings import Settings

if __name__ == '__main__':
    settings: Settings = Settings()
    discord_bot: DiscordBot = DiscordBot(settings.token)
    discord_bot.run()