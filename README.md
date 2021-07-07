# BasicBot:
It's a basic scalable Discord Bot made in Python & Discord.py. It contain a simple embed content load and a scalable command system.

# How to use:
Just add the bot token in `config.json` and run the main file. The code was divided into method groups according them functionalities. If you want to add a new command, just go to `commands`, add a new fuction with the same structure to the others and finally add the command key name to the dictionary called "method", now you can use your own command in discord.

To make your own embed, you only need to clone the `template.json` file and add the content. If you want to use an embed that you made, you only need to call the `load_content` method from the bot, and pass the name of your .json file as an argument and pass the output of the last method to the function `create_embed` and now you've done an discord embed, try to send it in a channel like your in your own server.

# Embed Testing:
<img src = "https://media.discordapp.net/attachments/810336186010697748/832304526697955328/unknown.png">

# Method List:

## client.views
```python
def load_embed(jsonfile_name : str) -> dict:
    pass # Load embed content from the 'assets/embeds' path

def create_embed(embed_content : dict) -> object:
    pass # Create an embed object from the embed content
```

## client.utils
```python
def is_DMChannel(message : str) -> bool:
    pass # Returns True if the message comes from a private channel

def is_Command(message : str) -> str, list:
    pass # Returns Command & Arguments if the message start with Command Prefix
```

# Projects that use BasicBot:
- https://github.com/HectorPulido/Awesome-discord-bot

