# BasicBot:
It's an basic scalable Discord Bot made in Python & Discord.py. It contain a simple embed content load and a scalable command system.

# How to use:
Just add the bot token in `config.json` and run the main file. The code was divided into function groups according them functionalities. If you want to add a new command, just go to Command Group `Funciones de Comando`, add a new fuction with the same structure to the others and finally add the command key name to the dictionary called "switch_method", now you can use your own command in discord.

To make your own embed, you only need to clone the `template.json` file and add the content. If you want to use an embed that you made, you only need to call the `load_content` method from the bot, and pass the name of your .json file as an argument and pass the output of the last method to the function `create_embed` and now you've done an discord embed, try to send it in a channel like your in your own server.

# Method List:
```python3
def load_content(jsonfile_name : str) -> dict:
    pass # Load json files from the 'assets/embeds' path

def create_embed(embed_content : dict) -> object:
    pass # Create an embed object from the embed content

def is_DMChannel(message : str) -> bool:
    pass # Returns True if the message comes from a private channel

def is_Command(message : str) -> str, list:
    pass # Returns Command & Arguments if the message start with Command Prefix
```


