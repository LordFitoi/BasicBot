import discord
from core.models.mixins import CommandsMixin

class Client(discord.Client, CommandsMixin):
    def __init__(self, **kargs):
        super().__init__()

        self.config = kargs.get("config")
        self.main_path = kargs.get("main_path")

        self.commands = {
            "example": self.cmd_example,
            "embed": self.cmd_embed
        }

    async def eval_commands(self, message: str) -> None:
        command, arguments = self.is_Command(message)

        if command and command in self.commands:
            await self.commands[command](message, arguments)
            self.log_Message(message)

    async def on_ready(self) -> None:
        print(f"@ Logged as {self.user}")

    async def on_message(self, message: object) -> None:
        if not message.author.bot and not self.is_DMChannel(message):
            await self.eval_commands(message)