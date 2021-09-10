from json.decoder import JSONDecoder
from typing import Dict
import requests
import json

decoder = JSONDecoder()

def geocode(addr, key="Osf7NeGQC6pA19cCBwSsId40uv6RCZ8o", limit=1):
    addr.replace(' ', "%20")
    r = requests.get(f'https://api.tomtom.com/search/2/geocode/{addr}.json??typeahead=false&limit={limit}&key={key}')
    a = str(r.json())
    a.replace('\'', '\"')
    j = decoder.decode(a)
    lat = j['results']['position']['lat']
    lon = j['results']['position']['lon']
    coords = [lat, lon]
    return coords
    #toFile(j)


        
def reverseGeocode(coords, key='Osf7NeGQC6pA19cCBwSsId40uv6RCZ8o', limit=1):
    lat=coords[0]
    lon=coords[1]
    r = requests.get(f'https://api.tomtom.com/search/2/reverseGeocode/{lat}%2C{lon}.json?key={key}')
    a = str(r.json())
    a.replace('\'', '\"')
    j = decoder.decode(a)
    addr = j['addresses']['address']['freeformAddress']
    return addr
    #toFile(j)

def toFile(f):
    with open("temp.txt", 'w') as file:
        file.write(str(f))
