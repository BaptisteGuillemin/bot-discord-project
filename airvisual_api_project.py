# -*- coding: utf-8 -*-
"""AirVisual_API_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KGfGPiJGVAEgo_WOgxpUthfwQDOqV7hs
"""
import pandas as pd
import requests
import plotly.express as plt
import plotly.graph_objects as go
APIkey = "19e55afb-07fc-4b68-b3b8-74c7950f0aee"
df = pd.DataFrame(columns = ['country', 'state', 'city', 'latitude', 'longitude', 'AQI'])

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
    color_scale = [(0, 'lime'), (0.2, 'green'), (0.3, 'yellow'), (0.4, 'orange'), (0.6, 'red'), (1,'black')]
    range_color = [1, 500]

    fig = plt.scatter_mapbox(df, lat="longitude", lon="latitude", hover_name="city", hover_data=["city", "AQI"], opacity=1,
                            color="AQI", color_continuous_scale= color_scale, range_color=range_color,
                            size='AQI', size_max=10, zoom=6, height=400, width=500)

    fig.update_layout(mapbox_style='carto-positron')
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig.show()

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
    return fig.show()

#get_labels()

# get automatic zoom for the map, in case of multiple plot with far distance

def zoom_center(lons: tuple=None, lats: tuple=None, lonlats: tuple=None,
        format: str='lonlat', projection: str='mercator',
        width_to_height: float=2.0) -> (float, dict):
    """Finds optimal zoom and centering for a plotly mapbox.
    Must be passed (lons & lats) or lonlats.
    Parameters
    --------
    lons: tuple, optional, longitude component of each location
    lats: tuple, optional, latitude component of each location
    lonlats: tuple, optional, gps locations
    format: str, specifying the order of longitud and latitude dimensions,
        expected values: 'lonlat' or 'latlon', only used if passed lonlats
    projection: str, only accepting 'mercator' at the moment,
        raises `NotImplementedError` if other is passed
    width_to_height: float, expected ratio of final graph's with to height,
        used to select the constrained axis.
    Returns
    --------
    zoom: float, from 1 to 20
    center: dict, gps position with 'lon' and 'lat' keys

    >>> print(zoom_center((-109.031387, -103.385460),
    ...     (25.587101, 31.784620)))
    (5.75, {'lon': -106.208423, 'lat': 28.685861})
    """
    if lons is None and lats is None:
        if isinstance(lonlats, tuple):
            lons, lats = zip(*lonlats)
        else:
            raise ValueError(
                'Must pass lons & lats or lonlats'
            )
    
    maxlon, minlon = max(lons), min(lons)
    maxlat, minlat = max(lats), min(lats)
    center = {
        'lon': round((maxlon + minlon) / 2, 6),
        'lat': round((maxlat + minlat) / 2, 6)
    }
    
    # longitudinal range by zoom level (20 to 1)
    # in degrees, if centered at equator
    lon_zoom_range = np.array([
        0.0007, 0.0014, 0.003, 0.006, 0.012, 0.024, 0.048, 0.096,
        0.192, 0.3712, 0.768, 1.536, 3.072, 6.144, 11.8784, 23.7568,
        47.5136, 98.304, 190.0544, 360.0
    ])
    
    if projection == 'mercator':
        margin = 1.2
        height = (maxlat - minlat) * margin * width_to_height
        width = (maxlon - minlon) * margin
        lon_zoom = np.interp(width , lon_zoom_range, range(20, 0, -1))
        lat_zoom = np.interp(height, lon_zoom_range, range(20, 0, -1))
        zoom = round(min(lon_zoom, lat_zoom), 2)
    else:
        raise NotImplementedError(
            f'{projection} projection is not implemented'
        )
    
    return zoom, center

'''user_answer = input("Did you want to check and plot on a map the air quality somewhere ? yes or no")
if user_answer.lower() == 'no': print("Ok, an another time")
else: 
    countries = get_all_countries()
    print("Select a country by copy and past")

    while True:
      print(countries)
      country = input('In which country are you interested to know the current AQI ?')
      if country == "no": break
      else: print(get_state(country)) 

      state = input('In which state are you interested to know the current AQI ?')
      print(get_city(state, country))

      city = input('In which city are you interested to know the current AQI ?')
      DF = DF.append(get_aqius(city, state, country))  
      # print visualisation
      map_df()
      get_labels()

      loop = input("Would like to plot another city's AQI on the map ? yes or no")
      if loop == "no": break'''

