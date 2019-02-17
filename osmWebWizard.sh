#!/bin/bash

# @ filename osmWebWizard.sh
# @ author   Yuji Ogusu
# @ date     2019/02/17

if [ ! -d ./osm ]; then
	mkdir osm
fi
cd osm
TOOLS_DIR=$SUMO_HOME/tools
$TOOLS_DIR/osmWebWizard.py
