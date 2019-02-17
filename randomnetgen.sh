#!/bin/bash
mkdir randommap
netgenerate --rand \
    --rand.random-lanenumber \
    --rand.random-priority \
    --rand.grid \
    --tls.guess \
	--output-file randommap/map.net.xml 
