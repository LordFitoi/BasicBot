import json, os
from core.models.client import Client
from discord_slash import SlashCommand

main_path = os.path.dirname(__file__)
config_path = os.path.join(main_path, "config.json")

with open(config_path, "r") as jsonfile:
    config: dict = json.load(jsonfile)

if __name__ == "__main__":
    Client(**config).run()
