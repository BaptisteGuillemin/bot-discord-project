import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTAzNDc2MTQ4NDMwNTE4Njg3Ng.GQt7gk.RexGUYAlgVVKBjbeEcvuglQUOLrWX9-iA5KVpk')