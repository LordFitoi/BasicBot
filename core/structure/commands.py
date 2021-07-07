
class Commands:
    """
     # --- # Glosario # --- #
    methods: object -> It's a dict with the name and
    what method it'll call for each command.
    """
    def __init__(self, client: object):
        self.views = client. views
        self.methods = {
            "example" : self.cmd_example,
            "embed" : self.cmd_embed
        }

    async def cmd_example(self, message : str, arguments : list) -> None:
        await message.channel.send(f"Esto es un comando de prueba, argumentos({arguments})")

    async  def cmd_embed(self, message : str, arguments : list) -> None:
        # Load embed templates:
        embed_content: dict = self.views.load_embed("test_embed")
        embed: object = self.views.create_embed(embed_content)

        # Send the embed to the user:
        await message.channel.send(embed = embed)
