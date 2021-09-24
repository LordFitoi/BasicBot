import discord, json
from os.path import join
from discord.ext.commands import Command

class UtilsMixin:    
    def is_DMChannel(self, message: discord.Message) -> bool:
        return isinstance(message.channel, discord.channel.DMChannel)

    def log_Message(self, message: discord.Message): 
        if self.is_debug:
            print(f"{message.author} : {message.content}")

    def log_Commands(self):
        if self.is_debug:
            print("@ Command List\n# ---------- #")
            
            for index, command_name in enumerate(self.commands):
                print(f"{index}) {command_name}")
            
            print("# ---------- #\n")
    
    def get_Commands(self, prefix="cmd_"):
        '''Add as command all methods with the prefix in them name'''

        for attr_name in dir(self):
            attr = getattr(self, attr_name)

            if callable(attr) and attr_name.startswith(prefix):
                command_kargs = {
                    "name": attr_name[len(prefix):],
                    "description": attr.__doc__
                }
                command = self.slash.slash(**command_kargs)(attr)
                self.slash.add_slash_command(command, **command_kargs)

        self.log_Commands()


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

        footer_text = f'Powered by: LordFitoi/BasicBot v{self.version}'
        
        embed.set_footer(text = footer_text)
        return embed
