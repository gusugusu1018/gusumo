#!/bin/bash
$SUMO_HOME/tools/visualization/plot_net_speeds.py -n gridmap/map.net.xml \
 --edge-width .5 -o speeds.png \
 --minV 0 --maxV 60 --xticks 16 --yticks 16 \
 --xlabel [m] --ylabel [m] --xlabelsize 16 --ylabelsize 16 
# --colormap jet
#--xlim 0,60 --ylim 0,60 \
