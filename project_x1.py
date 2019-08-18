import folium

#map = folium.Map(location=[80,-100])
#map.save('map.html')
map = folium.Map(location=[12.92,77.61])
fg = folium.FeatureGroup(name="my map")
fg.add_child(folium.Marker(location=[12.92,77.61],popup="I am a Makers", icon=folium.Icon(color="red")))
fg.add_child(folium.Marker(location=[11.92,77.61],popup="I am a Makers", icon=folium.Icon(color="red")))

map.add_child(fg)
map.save('map.html')
print(map)