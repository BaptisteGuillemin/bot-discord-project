'''
To Activate virtual environments
venv\Scripts\activate.bat
deactivate
'''

import airvisual_api_project as API_Visu
import discord

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
        await message.channel.send("Here is the example")
        print(f'message author: {message.author}')
        print(f'message content: {message.content}')
        API_Visu.get_default_visu('Paris', 'Ile-de-France', 'France')
        

        Map = discord.File("map.png", filename="map.png")
        Table = discord.File("table.png", filename="table.png")

        embed1 = discord.Embed(title="**AQI in Paris**", url = 'https://www.epa.gov/sites/default/files/2019-07/aqitableforcourse.png', description="Default example", color=0x6AA84F) #creates embed
        embed1.set_image(url="attachment://map.png")

        embed2 = discord.Embed(description="Labels description", color=0x6AA84F)
        embed2.set_image(url="attachment://table.png")

        await message.channel.send(file = Map, embed = embed1)
        await message.channel.send(file = Table, embed = embed2)
       


            
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

        API_Visu.get_default_visu(Selected_city, Selected_state, Selected_country)
        

        Map = discord.File("map.png", filename="map.png")
        Table = discord.File("table.png", filename="table.png")

        embed1 = discord.Embed(title="AQI in" + Selected_city, url = 'https://www.epa.gov/sites/default/files/2019-07/aqitableforcourse.png', description=Selected_city + ', ' + Selected_state + ', ' + Selected_country, color=0x6AA84F) #creates embed
        embed1.set_image(url="attachment://map.png")

        embed2 = discord.Embed(description="Labels description", color=0x6AA84F)
        embed2.set_image(url="attachment://table.png")

        await message.channel.send(file = Map, embed = embed1)
        await message.channel.send(file = Table, embed = embed2)

client.run(TOKEN)