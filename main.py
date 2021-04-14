import discord, json, os

main_path = os.path.dirname(__file__)
""" Carga la Configuracion del Bot"""
config_path = os.path.join(main_path, "config.json")
with open(config_path, "r") as jsonfile:
    bot_config = json.load(jsonfile)


class BotClient(discord.Client):

    """
    # --- # Nombre de Grupo # --- #
    Funciones de Contenido: Trabajan con el contenido como embeds
    imagenes, textos, etc...
    """
    def load_content(self, name: str) -> dict:
        """Carga contenido .json de la carpeta assets/embeds"""
        embed_path = os.path.join(main_path, f"assets/embeds/{name}.json")
        with open(embed_path, "r", encoding = "utf-8") as jsonfile:
            content = json.load(jsonfile)

        return content

    def create_embed(self, content: dict) -> object:
        """Crea un embed basado en el contenido de un diccionario"""
        embed = discord.Embed(
            title = content["title"],
            description = content["description"],
            color = int(content["color"], 16),
        )

        # Añade una miniatura a la pagina:
        embed.set_thumbnail(url = content["thumbnail"])

        # Añade texto en el cuerpo de la pagina:
        for key, value in content["content"].items():
            embed.add_field(name = key, value = value, inline = content["inline"])

        # Añade texto en pie de pagina:
        footertext = f'Powered by: LordFitoi/BasicBot v{bot_config["Version"]}'
        embed.set_footer(text = footertext)
        return embed


    """
    # --- # Nombre de Grupo # --- #
    Funciones Condicionales: Sirven como acortadores para una condicion
    compleja o que poseea un procedimiento.
    """
    @staticmethod
    def is_DMChannel(message: str) -> bool:
        """Verifica si es un mensaje proveniente es de un canal privado"""
        return isinstance(message.channel, discord.channel.DMChannel)

    @staticmethod
    def is_Command(message: str) -> list:
        """
        Verifica si comienza con el prefijo del bot, en caso de ser verdadero
        devuelve el nombre del comando y los argumentos. En caso contrario
        devuelve None.
        """
        content = message.content
        command, arguments = None, None

        if content.startswith(bot_config["Prefix"]):
            arguments = content[len(bot_config["Prefix"]):].lower().split()
            
            if arguments:
                command = arguments.pop(0)
                
        return command, arguments

    """
    # --- # Nombre de Grupo # --- #
    Funciones de Comando: Estas funciones son llamadas si el usuario
    nombra el comando correcto.

    # --- # Glosario # --- #
    switch_method: object -> En ella se contiene las funciones que se
    ejecutaran en dado caso de que un comando sea mencionado.
    """
    
    async def cmd_example(self, message : str, arguments : list) -> None:
        await message.channel.send(f"Esto es un comando de prueba, argumentos({arguments})")

    async  def cmd_embed(self, message : str, arguments : list) -> None:
        # Carga la plantilla de los embeds:
        embed_content = self.load_content("test_embed")
        embed = self.create_embed(embed_content)

        # Envia el embed por el canal proveniente del usuario:
        await message.channel.send(embed = embed)

    # Diccionario como metodo switch:
    switch_method = {
        "example" : cmd_example,
        "embed" : cmd_embed
    }


    """
    # --- # Nombre de Grupo # --- #
    Funciones de Evento: Estas funciones se encargan de realizar
    acciones cuando sucede un evento ocurre en Discord.

    # --- # Glosario # --- #
    message: object -> Mensaje del Usuario
    self.user: object -> Objeto Bot
    """
    async def on_ready(self) -> None:
        print(f"@ Registrado como # --- #{self.user}# --- #")

    async def on_message(self, message: object) -> None:
        if not message.author.bot and not self.is_DMChannel(message):
            """
            # --- # Escribe tu codigo aqui # --- #
            """
            # Verifica si esta en modo Debug:
            if bot_config["DebugMode"]:
                print(f"User {message.author}, Text: {message.content} \n")
            
            # Verifica si se menciono un comando:
            command, arguments = self.is_Command(message)
            if command and command in self.switch_method:
                # Ejecuta el comando mencionado:
                await self.switch_method[command](self, message, arguments)

if __name__ == "__main__":
    BotClient().run(bot_config["BotToken"])

