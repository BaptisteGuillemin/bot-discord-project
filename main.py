import discord
import pandas as pd

APIkey = "19e55afb-07fc-4b68-b3b8-74c7950f0aee"
df = pd.DataFrame(columns = ['country', 'state', 'city', 'latitude', 'longitude', 'AQI'])



## Bot informations 
TOKEN = 'MTAzNDc2MTQ4NDMwNTE4Njg3Ng.GsaN-j.kBmI7RH-Pz6P5YPFheKsb7RIEd7g0pL9Rb6_uk'
##Discord channel also know as guild
GUILD = 'PGE4 ADAV 2022-23'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

List_countries = ['France','Spain']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.content.startswith('$countries'):
        channel = message.channel
        await message.channel.send('Here are the countries where I can provide you the Air Quality Index')
        await message.channel.send(List_countries)

        def check_country(m):
            return m.content in List_countries and m.channel == channel

        msg = await client.wait_for('message', check=check_country)
        Selected_country = msg.content
        await message.channel.send('Here is the country selected : ' + Selected_country)
        await message.channel.send('After that I will need the State where you want to see the AQI')
        await message.channel.send('Here is the list of the States that you can choose')
        await message.channel.send(List_states)

        def check_State(m):
            return m.content in List_countries and m.channel == channel
client.run(TOKEN)