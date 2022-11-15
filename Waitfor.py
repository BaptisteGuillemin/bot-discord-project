import discord
import pandas as pd
import plotly.express as plt
import plotly.graph_objects as go

APIkey = "19e55afb-07fc-4b68-b3b8-74c7950f0aee"
df = pd.DataFrame(columns = ['country', 'state', 'city', 'latitude', 'longitude', 'AQI'])



## Bot informations 
TOKEN = 'MTAzNDc2MTQ4NDMwNTE4Njg3Ng.G_TVT4.UsDstUP1bUC3SoQdqmcUkmxOF66z9ERFcuk_wQ'
##Discord channel also know as guild
GUILD = 'PGE4 ADAV 2022-23'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
List_countries['France','Spain']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content in List_countries and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')
client.run(TOKEN)