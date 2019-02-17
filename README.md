# Environment
* ubuntu16.04
* sumo-1.1.0
* python (higher than 2.7)
* matplotlib
* pyproj
* rtree

# Setup
## set environment value
if you use bash
```
echo "export SUMO_HOME=/usr/share/sumo" >> ~/.bashrc
source ~/.bashrc
```

## Install matplotlib
```
# if you use python on system, you need `sudo -H` 
pip install matplotlib
```

## Install rtree and pyproj
rtree need spatialindex
```
wget http://download.osgeo.org/libspatialindex/spatialindex-src-1.8.5.tar.gz
cd spatialindex-src-1.8.5
mkdir build
cd build
cmake ..
make -j 4
sudo make install
sudo ldconfig
# if you use python on system, you need `sudo -H` 
pip install pyproj
pip install rtree
```

# How to use
## make grid map
```
./gridnetgen.sh
```

## draw net
```
./draw_net.py -n gridmap/map.net.xml
```
<img src="https://github.com/minaminoki/gusumo/blob/master/img/draw_gridmap.png" width="640">

## run simple simulation
```
./runner.py gridmap
# or
./runner.sh gridmap
```

## plot net speed
```
./plot_net_speed.sh
```

# How to SUMO?
## Prepare Map
* netgenerate
* netedit
* OpenStreatMap
## Demand Modeling
* random Trips
## Route generate
* duarouter
## Simulation
* sumo
* sumo-gui

# MEMO
map.net.xml
```
...
    <location netOffset="0.00,0.00" convBoundary="0.00,0.00,60.00,60.00" origBoundary="0.00,0.00,60.00,60.00" projParameter="!"/>
...
```
convBoundary is important

you use this number in plot\_net\_speed.py
```
...
 --xlim 0,60 --ylim 0,60 \
...
```

