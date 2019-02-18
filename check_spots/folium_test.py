#!/bin/bash

# @ filename newyork_convenience.sh
# @ author   Yuji Ogusu
# @ date     2019/02/17

import folium

folium_map = folium.Map(location=[40.738, -73.98],zoom_start=13,tiles="CartoDB dark_matter")
folium.PolyLine([[40.0,-73.0],[41,-74]]).add_to(folium_map)
folium_map.save("map.html")

#map.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]])

