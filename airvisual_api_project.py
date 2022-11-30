# -*- coding: utf-8 -*-
"""AirVisual_API_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KGfGPiJGVAEgo_WOgxpUthfwQDOqV7hs
"""
import pandas as pd
import numpy as np
import requests
import plotly.express as plt
import plotly.graph_objects as go
import plotly.io as pio

APIkey = "19e55afb-07fc-4b68-b3b8-74c7950f0aee"
DF = pd.DataFrame(columns = ['country', 'state', 'city', 'latitude', 'longitude', 'AQI'])

"""##Principals functions to process data"""

# Get list of all countries available

def get_all_countries():
    try:
        url = "http://api.airvisual.com/v2/countries?key=19e55afb-07fc-4b68-b3b8-74c7950f0aee"
        dic = requests.get(url).json()
        dic = dic['data']
        countries = [n['country'] for n in dic]
        return countries
    except:
        return print("erreur avec l'API ")

#get_all_countries()

# Get list of states: return dictionnary of the country parameter as key value and list of states as value

def get_state(country):
    try:
        url = 'http://api.airvisual.com/v2/states?country={}&key={}'.format(country, APIkey)
        dic = requests.get(url).json()
        dic = dic['data']
        states = [n['state'] for n in dic]
        return states
    except:
        return print("erreur avec l'API, trop de requête ")

#get_state("India")

# Get list of city from country and state parameter 
# return dictionnary: key: state / value: list of cities

def get_city(state, country):
    try:
        url = "http://api.airvisual.com/v2/cities?state={}&country={}&key={}".format(state, country, APIkey)
        dic = requests.get(url).json()
        dic = dic['data']
        city = [n['city'] for n in dic]
        return city
    except:
        return print("erreur avec l'API ")

#get_city('Delhi', 'India')

# Get Air quality level of a city
# return df

def get_aqius(city, state, country):
    try:
        df = pd.DataFrame(columns = ['country', 'state', 'city', 'latitude', 'longitude', 'AQI'])
        dic = {}
        URL = 'http://api.airvisual.com/v2/city?city={}&state={}&country={}&key={}'.format(city, state, country, APIkey)
        data = requests.get(URL).json()

        dic['country']= country
        dic['state']= state
        dic['city']= city
        dic['latitude'] = data['data']['location']['coordinates'][0]
        dic['longitude']= data['data']['location']['coordinates'][1]
        dic['AQI']= data['data']['current']['pollution']['aqius']

        df = df.append(dic, ignore_index=True)
        df['AQI'] = pd.to_numeric(df["AQI"])

        range_1 = range(0, 50)
        if dic['AQI'] in range_1: df['AQI label'] = "good"
        range_2 = range(50, 100)
        if dic['AQI'] in range_2: df['AQI label'] = "Moderate"
        range_3 = range(100, 150)
        if dic['AQI'] in range_3: df['AQI label'] = "Unhealthy for sensitive groups"
        range_4 = range(150, 200)
        if dic['AQI'] in range_4: df['AQI label'] = "Unhealthy"
        range_5 = range(200, 300)
        if dic['AQI'] in range_5: df['AQI label'] = "Very Unhealthy"
        range_6 = range(300, 500)
        if dic['AQI'] in range_6: df['AQI label'] = "Hazardous"

        return df

    except:
        return print("erreur avec l'API ")

"""## Visualization functions


"""

def map_df(df):
    df['AQI'] = pd.to_numeric(df["AQI"])  # to avoid size error
    color_scale = [(0, 'lime'), (0.2, 'green'), (0.3, 'yellow'), (0.4, 'orange'), (0.6, 'red'), (1,'black')]
    range_color = [1, 500]

    fig = plt.scatter_mapbox(df, lat="longitude", lon="latitude", hover_name="city", hover_data=["city", "AQI"], opacity=1,
                            color="AQI", color_continuous_scale= color_scale, range_color=range_color,
                            size='AQI', size_max=10, zoom=10, height=800, width=1000)

    fig.update_layout(mapbox_style='carto-positron')
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return pio.write_image(fig, "map.png")

#map_df(df)

def get_labels():
    colorscale = ['lime','green','yellow','orange','red','black']
    PAPER_BGCOLOR = '#f5f2d0'
    BGCOLOR = 'LightSteelBlue'

    fig = go.Figure(data=[go.Table(
        columnorder = [1,2,3,4],
        columnwidth = [50,70,60,400],
        
        header=dict(values=['<b>AQI</b>', '<b>Remark</b>','<b>Colour Code</b>','<b>Possible Health Effects</b>'],
                    line_color='darkslategray',
                    fill_color='skyblue',
                    align='left'),
        cells=dict(values=[['0-50','51-100','101-150','151-200','201-300','301-500'],
                          ['Good','Satisfactory','Moderate','Poor','Very Poor','Severe'],
                          ['','','','','',''],
                          ['Minimal impact','Minor breathing discomfort to sensitive people',\
                          'Breathing discomfort to the people with lungs, asthma and heart diseases',\
                          'Breathing discomfort to most people on prolonged exposure',\
                          'Respiratory illness on prolonged exposure','Affects healthy people and seriously impacts those with existing diseases']],
                  line_color='darkslategray',
                  fill_color=['rgb(255,255,255)',
                              'rgb(255,255,255)',
                                [color for color in colorscale],
                              'rgb(255,255,255)'],
                  align='left'))
    ])

    fig.update_layout(height=180,paper_bgcolor='LightSteelBlue',margin=dict(l=5,r=5,t=5,b=5))
    return pio.write_image(fig, "table.png")





def get_default_visu(city,state,country):
    DF = pd.DataFrame(columns = ['country', 'state', 'city', 'latitude', 'longitude', 'AQI'])
    DF = DF.append(get_aqius(city, state, country))
    map_df(DF)
    get_labels()