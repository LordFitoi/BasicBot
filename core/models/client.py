import discord
from os.path import dirname
from discord.ext.commands import Bot
from discord_slash import SlashCommand

from core.models.mixins import UtilsMixin, ViewsMixin
from core.models.commands import Commands


Mixins = [UtilsMixin, ViewsMixin]

class Client(Bot, Commands, *Mixins):
    main_path = dirname(dirname(dirname(__file__)))

    def __init__(self, **kargs):
        self.version  = kargs.get("version")
        self.token    = kargs.get("bot_token")
        self.prefix   = kargs.get("prefix")
        self.is_debug = kargs.get("debug_mode")
    
        super().__init__(command_prefix=self.prefix)
        self.slash = SlashCommand(self, sync_commands=True)

    def run(self):
        self.get_Commands()
        super().run(self.token)

    async def on_ready(self) -> None:
        print(f"@ Logged as {self.user}\n")

    async def on_message(self, message: discord.Message):
        await super().on_message(message)

        if not message.author.bot and not self.is_DMChannel(message):
            self.log_Message(message)