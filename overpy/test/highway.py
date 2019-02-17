#!/usr/bin/env python

# @file		highway.py
# @author	Yuji Ogusu
# @date		2019-02-17

import overpy

type = 'highway'

lat = 34.4461
lon = 133.2315 

api = overpy.Overpass()
result = api.query("""
    way(%f, %f, %f, %f) [%s];
    (._;>;); 
   out body;
    """ % (lat - 0.01, lon - 0.01, lat + 0.01, lon + 0.01, type) )

for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))

