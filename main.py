import discord, json

with open("settings.json","r") as f:
    settings = json.loads(f.read())



client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user: return


client.run()