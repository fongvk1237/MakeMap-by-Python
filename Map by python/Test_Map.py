import folium
import pandas

map=folium.Map(location=[13.7278956,100.52412349999997])

data=pandas.read_csv("https://raw.githubusercontent.com/kongruksiamza/PythonWebMap/master/province_th.csv")

city=list(data["City"])
lat=list(data["LAT"])
lon=list(data["LON"])

print(city)

fg=folium.FeatureGroup(name="Thailand Map")

fg.add_child(folium.Marker(location=[13.7278956,100.52412349999997],popup="cafe Bangkok"))
fg.add_child(folium.Marker(location=[13.8199206,100.06216760000007],popup="My Home"))

map.add_child(fg)

map.save("Map1.html")