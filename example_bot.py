# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#Etape 1 (hello)
    if message.content.startswith('hello'):
        await message.channel.send(f'Hello!! {message.author.name}')
        await message.channel.send('Did you want to check and plot on a map the air quality somewhere ? Yes or No.')
#Etape 2 (yes or no)
    if message.content.lower() == 'no':
        await message.channel.send(f'Okay {message.author.name}, let me know when I will be able to help you, hope to see you soon !')
    if message.content.lower() == 'yes':
        await message.channel.send('Here are the countries where I can provide you the Air Quality Index')
        await message.channel.send('function get All country')
        await message.channel.send("--------")
        await message.channel.send('In which country are you interested to know the current Air Quality Index ?')
        await message.channel.send("Bot developpement in progress...")
'''

user_answer = input("Did you want to check and plot on a map the air quality somewhere ? yes or no")
while True:
  count=0
  print(get_all_countries())
  country = input('In which country are you interested to know the current AQI ?')
  if country == "no": break
  else: print(get_state(country)) 

  state = input('In which state are you interested to know the current AQI ?')
  print(get_city(state, country))

  city = input('In which city are you interested to know the current AQI ?')

  if count > 0: df = df.append(get_aqius(city, state, country))
  else: df = get_aqius(city, state, country)
  
  map_df()
  get_labels()

  loop = input("Would like to plot another city's AQI on the map ? yes or no")
  if loop == "no": break
  else: count +=1'''




client.run('MTAzNDc2MTQ4NDMwNTE4Njg3Ng.G8kEmq.fILIt8muCpHVlrmek42IZXEDsKQm7b7xxg_iE4')