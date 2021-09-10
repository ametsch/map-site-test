import folium


def make(ls, path="map.html", center=[51.4934, 0.0098]):
    mapVar = folium.Map(center)
    for coords, popup in ls:
        folium.Marker(coords, popup=popup).add_to(mapVar)
    mapVar.save(f"templates/maps/{path}")
