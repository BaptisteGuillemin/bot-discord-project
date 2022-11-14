import discord
import pandas as pd
import plotly.express as plt
import plotly.graph_objects as go

APIkey = "19e55afb-07fc-4b68-b3b8-74c7950f0aee"
df = pd.DataFrame(columns = ['country', 'state', 'city', 'latitude', 'longitude', 'AQI'])



## Bot informations 
TOKEN = 'MTAzNDc2MTQ4NDMwNTE4Njg3Ng.G8kEmq.fILIt8muCpHVlrmek42IZXEDsKQm7b7xxg_iE4'
##Discord channel also know as guild
GUILD = 'PGE4 ADAV 2022-23'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

##To know about the bot id, discord channel and bot name
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

client.run(TOKEN)