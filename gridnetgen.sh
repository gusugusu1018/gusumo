#!/bin/bash

# @ filename gridnetgen.sh
# @ author   Yuji Ogusu
# @ date     2019/02/17

if [ -d ./gridmap ]; then
	rm -rf gridmap
fi
mkdir gridmap
netgenerate --grid \
	--grid.length 100 \
	--grid.number 10 \
	--default.lanenumber 2 \
	--default.speed 11.111 \
	--tls.guess \
	--output-file gridmap/map.net.xml
