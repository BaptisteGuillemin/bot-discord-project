# bot-discord-project

venv\Scripts\activate.bat
deactivate


Our bot plot the Air quality of a given city, state, country.
Following by a table presenting the index and what they means made with matplotlib.

As the API is not working for more than 3 or 4 request in a single function, and the list of countries, states and city that are available are not exhaustive. The methode is the following:
- 1st request to the API to get the list of all countries available
- then the state, in this given country
- finally the city, in this given state.

The bot display the 2 visualization with thoses 3 necessary parameters.

$Call_Bot to call the bot in the discord discussion
$Get_example is a example of visualization with pre define parameters of Paris, Ile-de-France, France.