ETAPE1 = 'Vide'
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        While ETAPE1 == 'Vide':
            await message.channel.send(f'Hello!! {message.author.name}')
            await message.channel.send('Did you want to check and plot on a map the air quality somewhere ? Yes or No.')
            await message.channel.send("--------")
            if message.content.lower() == 'no':
                await message.channel.send(f'Okay {message.author.name}, let me know when I will be able to help you, hope to see you soon !')
                await message.channel.send("--------")
                retourner debut du while
            if message.content.lower() == 'yes':
                ETAPE1 = message.content
                await message.channel.send('Here are the countries where I can provide you the Air Quality Index')
                await message.channel.send('function get All country')