import pandas as pd
import discord
import requests
import plotly.express as plt
import plotly.graph_objects as go

import airvisual_api_project as API_Visu


## Bot informations 
TOKEN = 'MTAzNDc2MTQ4NDMwNTE4Njg3Ng.GbTx7f.tS4ufSJ82oNMFXziItiK-9ommAqR9T2nDDu3bk'
##Discord channel also know as guild
GUILD = 'PGE4 ADAV 2022-23'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.content.startswith('$Call_Bot'):
        channel = message.channel
        await message.channel.send('I Can plot on a map the air quality or a city that we will choose !')
        await message.channel.send("--------")

        #Select the country
        list_countries = API_Visu.get_all_countries()
        await message.channel.send('Here are the countries where I can provide you the Air Quality Index')
        await message.channel.send(list_countries)

        def check_country(m):
            return m.content in list_countries and m.channel == channel

        msg_country = await client.wait_for('message', check=check_country)
        Selected_country = msg_country.content
        await message.channel.send('Here is the country selected : ' + Selected_country)
        await message.channel.send("--------")
        

        #Select the state
        states = API_Visu.get_state(Selected_country)
        await message.channel.send('After that I will need the State where you want to see the AQI')
        await message.channel.send('Here is the list of the States that you can choose')
        await message.channel.send(states)

        def check_State(m):
            return m.content in states and m.channel == channel
        
        msg_state = await client.wait_for('message', check=check_country)
        Selected_state = msg_state.content
        await message.channel.send('Here is the state selected : ' + Selected_state)
        await message.channel.send("--------")
        
        #Select the city
        List_cities = API_Visu.get_city(Selected_state, Selected_country)
        await message.channel.send('After that I will need the city where you want to see the AQI')
        await message.channel.send('Here is the list of the cities that you can choose')
        await message.channel.send(List_cities)

        def check_city(m):
            return m.content in List_cities and m.channel == channel
        
        msg_city = await client.wait_for('message', check=check_country)
        Selected_city = msg_city.content
        await message.channel.send('Here is the city selected : ' + Selected_city)
        await message.channel.send("--------")

        await message.channel.send("Here is the localisation selected : " + "Country : " + Selected_country + ", State : " + Selected_state + ", City : " + Selected_city)
client.run(TOKEN)