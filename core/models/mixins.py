import discord, json
from os.path import join

class UtilsMixin:    
    def is_DMChannel(self, message: str) -> bool:
        return isinstance(message.channel, discord.channel.DMChannel)

    def is_Command(self, message: str) -> list:
        prefix = self.config.get("Prefix")
        content = message.content

        if content.startswith(prefix):
            arguments = content[len(prefix):].lower().split()
            
            if arguments:
                command = arguments.pop(0)
                
                return command, arguments

    def log_Message(self, message: str) -> None: 
        if self.config["DebugMode"]:
            print(f"{message.author} : {message.content}")


class ViewsMixin:
    def load_embed(self, name: str) -> dict:
        """Load a embed content from assets/embeds"""

        embed_dir_path = join(self.main_path, f"assets/embeds")
        embed_path = join(embed_dir_path, f"{name}.json")

        with open(embed_path, "r", encoding = "utf-8") as jsonfile:
            content = json.load(jsonfile)

        return content

    def create_embed(self, content: dict) -> object:
        """Create a embed object"""
        
        title: str = content.get("title")
        thumbnail_url: str = content.get("thumbnail")
        description: str = content.get("description")
        content_list: dict = content.get("content")
        inline: bool = content.get("inline")
        color: str = content.get("color")

        embed = discord.Embed(
            title = title,
            description = description,
            color = int(color, 16),
        )

        embed.set_thumbnail(url = thumbnail_url)

        for key, value in content_list.items():
            embed.add_field(
                name = key,
                value = value,
                inline = inline
            )

        version = self.config.get("Version")
        footer_text = f'Powered by: LordFitoi/BasicBot v{version}'
        
        embed.set_footer(text = footer_text)
        
        return embed


class CommandsMixin(UtilsMixin, ViewsMixin):
    async def cmd_example(self, message: str, arguments: list):
        await message.channel.send(f"This is a test command, arguments: ({arguments})")

    async def cmd_embed(self, message: str, arguments: list):
        embed_content = self.load_embed("test_embed")
        embed = self.create_embed(embed_content)

        await message.channel.send(embed = embed)
    