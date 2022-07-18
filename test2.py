import folium
map_2 = folium.Map(location=[29.7604, -95.3698], zoom_start=12,tiles='Stamen Terrain')
folium.Marker([29.969220045008328, -94.9886898766219], popup='Vehicle', icon=folium.Icon(color='red')).add_to(map_2)

map_2