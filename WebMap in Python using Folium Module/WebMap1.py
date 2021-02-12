import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon = list(data["LON"])
elev=list(data["ELEV"])
name= list(data["NAME"])

def col(ele):
    if ele < 1000:
        return 'lightblue'
    elif 1000<= ele < 3000:
        return 'pink'
    else:
        return 'darkpurple'     

map=folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name= "Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(nm) + "\n"+  str(el)+ "m", icon=folium.Icon(color= col(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
else 'blue' if 10000000 <= x['properties']['POP2005'] <= 20000000
else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")