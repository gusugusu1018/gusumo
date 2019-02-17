#!/bin/bash

# @ filename newyork_convenience.sh
# @ author   Yuji Ogusu
# @ date     2019/02/17

import os

import overpy
import folium
import dill

def main():
    file_name = './data/newyork_convenience.pkl'
    folium_map = folium.Map(location=[40.738, -73.98],zoom_start=13,tiles="CartoDB dark_matter")
    with open(file_name, 'rb') as f:
        result = dill.load(f)
    print(len(result.nodes))
    for node in result.nodes:
        print('(lon,lat) : ('+str(node.lon)+','+str(node.lat)+')')
        #folium.CircleMarker(location=[node.lat, node.lon]).add_to(folium_map)
        folium.Marker(location=[node.lat, node.lon], popup='convenience store').add_to(folium_map)
    folium_map.save("map.html")

if __name__ == "__main__":
    main()
map.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]])

