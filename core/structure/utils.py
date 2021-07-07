import discord

class Utils:
    def __init__(self, client: object):
        self.client: object = client

    @staticmethod
    def is_DMChannel(message: str) -> bool:
        return isinstance(message.channel, discord.channel.DMChannel)

    def is_Command(self, message: str) -> list:
        prefix: str = self.client.config.get("Prefix")
        content: str = message.content
        command, arguments = None, None

        if content.startswith(prefix):
            arguments: list = content[len(prefix):].lower().split()
            
            if arguments:
                command = arguments.pop(0)
                
        return command, arguments
