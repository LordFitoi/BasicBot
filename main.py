import json, os
from core.models.client import Client

main_path = os.path.dirname(__file__)

""" Load the bot configuration """
config_path = os.path.join(main_path, "config.json")

with open(config_path, "r") as jsonfile:
    bot_config: dict = json.load(jsonfile)

if __name__ == "__main__":
    client: object = Client(
        config = bot_config,
        main_path = main_path
    )

    bot_token: str = bot_config.get("BotToken")
    client.run(bot_token)
