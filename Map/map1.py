import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])
type_of = list(data["TYPE"])
circle_icon = False


words = """<h4>Volcano information:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m (%s feet)<br>
Type: %s
"""

def color_producer(e):
    if e < 1000:
        return "white"
    elif e < 2000:
        return "lightgray"
    elif e < 3000:
        return "gray"
    elif e < 4000:
        return "black"
    else:
        return "darkred"

def icolor_producer(t):
    if t == "Stratovolcano" or t == "Stratovolcanoes" or t == "Stratovolcano":
        return "green"
    elif t == "Caldera" or t == "Calderas":
        return "red"
    elif t == "Cinder cone" or t == "Cinder cones":
        return "orange"
    elif t == "Volcanic field":
        return "pink"
    elif t == "Maar" or t == "Maars":
        return "cadetblue"
    elif t == "Lava domes" or t == "Lava dome":
        return "darkpurple"
    elif t == "Shield volcano" or t == "Shield volcanoes":
        return "purple"
    elif t == "Complex volcano":
        return "blue"
    else:
        return "beige"
    

map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Toner")

fgv = folium.FeatureGroup(name = "Volcanoes")


for lt, ln, nm, el, ty in zip(lat, lon, name, elev, type_of):
    el_f = str(int(el * 3.28084))
    iframe = folium.IFrame(html=words % (nm, nm, str(el), el_f, ty), width=200, height=100)
    if circle_icon == True:
        fgv.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), tooltip = nm, fill_color = icolor_producer(ty), color = color_producer(el), radius = 7.5, fill_opacity = 10))
    else:
        fgv.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(iframe), icon = folium.Icon(color = icolor_producer(ty), icon_color = color_producer(el), angle = 45)))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding = "utf-8-sig").read(),
style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

fga = folium.FeatureGroup(name = "Area")

fga.add_child(folium.GeoJson(data=open("world.json", "r", encoding = "utf-8-sig").read(),
style_function = lambda y: {"fillColor":"gray" if y["properties"]["AREA"] > 100 else "green"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(fga)
map.add_child(folium.LayerControl())
map.save("Map1.html")

