#!/bin/bash
mkdir gridmap
netgenerate --grid \
	--grid.length 30 \
	--grid.number 3 \
	--default.lanenumber 2 \
	--default.speed 11.111 \
	--tls.guess \
	--output-file gridmap/map.net.xml
