#!/bin/bash

# @ filename spidernetgen.sh
# @ author   Yuji Ogusu
# @ date     2019/02/17

if [ -d ./spidermap ]; then
    rm -rf spidermap
fi
mkdir spidermap
netgenerate --spider \
    --spider.arm-number 5 \
    --spider.circle-number 3 \
    --default.lanenumber 2 \
	--default.speed 11.111 \
	--tls.guess \
	--output-file spidermap/map.net.xml