import discord

TOKEN = ""

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('`hello'):
        await message.channel.send('Hello ')
    if message.content.startswith('`help'):
        await message.channel.send('``` `hello, Hello```')

client.run(TOKEN)