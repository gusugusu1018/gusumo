#!/bin/bash

# @ filename randomnetgen.sh
# @ author   Yuji Ogusu
# @ date     2019/02/17

mkdir randommap
netgenerate --rand \
    --rand.random-lanenumber \
    --rand.random-priority \
    --rand.grid \
    --tls.guess \
	--output-file randommap/map.net.xml 
