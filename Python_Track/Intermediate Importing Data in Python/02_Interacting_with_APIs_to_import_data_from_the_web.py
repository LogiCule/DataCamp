#Loading and exploring a JSON

with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
for k in json_data.keys():
    print(k + ': ',json_data[k])
    
#API requests

import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
r = requests.get(url)
print(r.text)

#JSON–from the web to Python

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'
r = requests.get(url)
json_data = r.json()

#Checking out the Wikipedia API

import requests
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"
r = requests.get(url)
json_data = r.json()
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
