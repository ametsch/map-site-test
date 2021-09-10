import json

import folium
class ListClass:
    def __init__(self, list, name) -> None:
        self.list = list
        self.name = name
    def getList(self):
        return self.list
    def getName(self):
        return self.name
    def toJSON(self):
        with open(fr'static/out/{self.name}/{self.name}.json', 'w') as f:
            json.dump(self.list, f)
    def toTXT(self):
        with open(fr'static/out/{self.name}/{self.name}.txt', 'w') as f:
            f.write(self.list.__str__())
    def toHTML(self):
        mapVar = folium.Map()
        for coords, popup in self.list:
            folium.Marker(coords, popup=popup).add_to(mapVar)
        mapVar.save(fr"static/out/{self.name}/{self.name}.html")
    
