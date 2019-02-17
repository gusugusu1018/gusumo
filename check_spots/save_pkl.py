#!/bin/bash

# @ filename newyork_convenience.sh
# @ author   Yuji Ogusu
# @ date     2019/02/17

import os

import overpy
import dill

def main():
    key = "shop"
    tag = "convenience"
    prefs = "New York"
    api = overpy.Overpass()
    #"node(50.745,7.17,50.75,7.18);out;"
    query = (
        'area["name"~"{prefs}"];\n'
        'node(area)["{key}"="{tag}"];\n'
        'out;'
    ).format(prefs=prefs, key=key, tag=tag)
    print('Fetch query...')
    result = api.query(query)
    print('Fetch complete')
    filename = 'data/{}_{}.pkl'.format(key, tag)
    print('Save as {}'.format(filename))
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            dill.dump(result, f)
        print('Save complete.')

if __name__ == "__main__":
    main()
