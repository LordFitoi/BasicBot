import discord, json, os

class Views:
    def __init__(self, client: object):
        self.client = client
    
    def load_embed(self, name: str) -> dict:
        """Load a embed content from assets/embeds"""

        embed_dir_path = os.path.join(self.client.main_path, f"assets/embeds")
        embed_path = os.path.join(embed_dir_path, f"{name}.json")

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

        version: str = self.client.config.get("Version")
        footertext = f'Powered by: LordFitoi/BasicBot v{version}'
        
        embed.set_footer(text = footertext)
        
        return embed
