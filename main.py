import pandas as pd
import discord
import requests
import plotly.express as plt
import plotly.graph_objects as go

import airvisual_api_project as API_Visu


## Bot informations 
TOKEN = 'MTAzNDc2MTQ4NDMwNTE4Njg3Ng.GUgzR1.vnjE0PtnFrlaiAZThUG2K71b30pnJ5gxOcOSEI'
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
        await message.channel.send('I can plot on a map the air quality of a city that we will choose !')
        await message.channel.send("If you want to see an example, and visualize Paris's Air Quality, Answer: '$Get_example'. If not answer: '$My_Location' ")
        await message.channel.send("--------")
        print(f'message author: {message.author}')
        print(f'message content: {message.content}')

    if message.content.startswith('$Get_example') :    
        await message.channel.send("You have typped Yes")
        print(f'message author: {message.author}')
        print(f'message content: {message.content}')
        API_Visu.get_default_visu('Paris', 'Ile-de-France', 'France')
    
    message.channel.send
        


            
    if message.content.startswith('$My_Location'): 
        await message.channel.send("Let's choose where you want to visualize the Air Qualit Index !")
        print(f'message author: {message.author}')
        print(f'message content: {message.content}')

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
        
        msg_state = await client.wait_for('message', check=check_State)
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
        
        msg_city = await client.wait_for('message', check=check_city)
        Selected_city = msg_city.content
        await message.channel.send('Here is the city selected : ' + Selected_city)
        await message.channel.send("--------")

        await message.channel.send("Here is the localisation selected : " + "Country : " + Selected_country + ", State : " + Selected_state + ", City : " + Selected_city)

client.run(TOKEN)