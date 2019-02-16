#!/bin/bash
## filename sumo.sh
## author   Yuji Ogusu
## date     2019/02/16
## license  MIT

set -e

usage_exit() {
	cat <<_EOT_
Usage:
	`basename $0` -d MAP_DIR [-h] [-g] ...

Description:
	shell script for sumo

Options:
	-d MAP_DIR (necessary)
	-g use GUI (default CUI)
	-e set end time (default 2000)
	-h display help
_EOT_

        exit 1
}

TOOLS_DIR=/usr/share/sumo/tools
END_TIME=2000
USE_GUI=false

while getopts d:e:gh OPT
do
    case $OPT in
        d)  MAP_DIR=$OPTARG
            ;;
	g)  USE_GUI=true
	    ;;
	e)  END_TIME=$OPTARG
	    ;;
        h)  usage_exit
            ;;
        \?) usage_exit
            ;;
    esac
done

shift $((OPTIND - 1))

if [ "${MAP_DIR}" == "" ];then
	usage_exit
fi
cat <<_EOT_
using directory : $MAP_DIR
use GUI         : $USE_GUI
end time        : $END_TIME
_EOT_

LOG_DIR=`date '+%Y%m%d-%H%M%S'`

NET_FILE=$MAP_DIR/map.net.xml
TRIPS_FILE=$MAP_DIR/map.trips.xml
ROUTE_FILE=$MAP_DIR/map.rou.xml

echo "generate trips"
$TOOLS_DIR/randomTrips.py \
	--net-file $NET_FILE \
	--output-trip-file $TRIPS_FILE \
	--verbose
echo "generate route"
duarouter --route-files $TRIPS_FILE \
	--net-file $NET_FILE \
	--output-file $ROUTE_FILE \
	--ignore-errors \
	--xml-validation never
echo "start simulation"
mkdir $MAP_DIR/$LOG_DIR

SUMO_CMD="sumo"
if $USE_GUI ;then
	SUMO_CMD="sumo-gui"
fi
$SUMO_CMD --begin 0 --end $END_TIME \
	--net-file $NET_FILE \
	--route-files $ROUTE_FILE \
	--summary-output $MAP_DIR/$LOG_DIR/map.summary.xml \
	--fcd-output $MAP_DIR/$LOG_DIR/map.dump \
	--fcd-output.geo \
	--ignore-route-errors \
	--xml-validation never \
	--verbose
