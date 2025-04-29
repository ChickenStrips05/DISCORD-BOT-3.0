import discord, json, os
from pathlib import Path

with open("settings.json","r") as f:
    settings = json.loads(f.read())




def getAllCommands():
    commands = {}
    for file in Path("commands/").rglob("*.py"):
        if file.is_file():
            commands[file.stem] = str(file)
    return commands


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user: return
    if not message.content.startswith(settings["prefix"]): return
    text = message.content
    mentionIndex = 0
    channel = message.channel
    commands = getAllCommands()

    for command_text in text.split("|"):
        args = command_text.strip().split()
        
        for i, arg in enumerate(args):
            if arg.startswith("<@"):
                args[i] = message.mentions[mentionIndex]
                mentionIndex += 1

        command_name = args[0].replace(settings["prefix"], "")

        if command_name in commands:
            path = commands[command_name]
            class data:
                Client=client
                Message=message
                Text=text
                Channel=channel
                Commands=commands
                Args=args
                class modules:
                    Discord=discord
                    Json=json
                    Os=os
            
            try:
                with open(path,"r") as f:
                    localScope = {}
                    exec(f.read(),{},localScope)
                    await localScope["main"](data)
            except:
                await channel.send("An error occurred")
        else:
            await channel.send("Uknown command.")
            pass
        

client.run(settings["token"])