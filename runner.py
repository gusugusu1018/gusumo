#!/usr/bin/env python

# @file		runner.py
# @author	Yuji Ogusu
# @date		2019-02-16

import argparse
import commands
import sys
import os
import datetime

## Get Environment information
if 'SUMO_HOME' in os.environ:
   SUMO_PATH=os.environ['SUMO_HOME']
   TOOLS_PATH=os.path.join(SUMO_PATH, 'tools')
   BIN_PATH=os.path.join(SUMO_PATH,'bin')
   sys.path.append(TOOLS_PATH)
else:   
   sys.exit("please declare environment variable 'SUMO_HOME'")

## Set Argument Parser
parser = argparse.ArgumentParser(description='script for sumo') 
parser.add_argument('mapdirectory',help='directory include map.net.xml')
parser.add_argument('-c','--cui',type=bool,default=False,help='use CUI (default False)')
parser.add_argument('-e','--endtime',type=str,default='2000',help='set simulation time (default 2000)')

args = parser.parse_args()

MAP_DIR=str(args.mapdirectory)
print('sumo home       : '+SUMO_PATH)
print('bin path        : '+BIN_PATH)
print('tools path      : '+TOOLS_PATH)
print('using directory : '+MAP_DIR) 
print('use CUI         : '+str(args.cui))
print('end time        : '+str(args.endtime))

NET_FILE=args.mapdirectory+'/map.net.xml'
TRIPS_FILE=args.mapdirectory+'/map.trips.xml'
ROUTE_FILE=args.mapdirectory+'/map.rou.xml'


## Generate Trips Using srandomTrips.py in sumo-tools
print("\033[36mGenerate trips\033[0m")

tripsgen_cmd = os.path.join(TOOLS_PATH , 'randomTrips.py') \
	+ ' --net-file ' + NET_FILE \
	+ ' --output-trip-file ' + TRIPS_FILE \
	+ ' --verbose '
out = commands.getoutput(tripsgen_cmd)
print(out)

## Generate route Using duarouter in sumo
print("\033[36mGenerate route\033[0m")

routgen_cmd = os.path.join(BIN_PATH,'duarouter') \
	+ ' --route-files ' + TRIPS_FILE \
	+ ' --net-file ' + NET_FILE \
	+ ' --output-file ' + ROUTE_FILE \
	+ ' --ignore-errors ' \
	+ ' --xml-validation never '
out = commands.getoutput(routgen_cmd)
print(out)

## Start SUMO 
print("\033[36mStart simulation\033[0m")
now = datetime.datetime.now()
LOG_DIR=os.path.join(MAP_DIR,"log",now.strftime("%Y%m%d%H%M%S"))
os.makedirs(LOG_DIR)
print("make Directory for log : "+LOG_DIR)

SUMO_CMD='sumo-gui'
if args.cui :
	SUMO_CMD='sumo'

sim_cmd = os.path.join(BIN_PATH,SUMO_CMD) \
	+ ' --begin 0 --end ' + args.endtime \
	+ ' --net-file ' + NET_FILE \
	+ ' --route-files ' + ROUTE_FILE \
	+ ' --summary-output ' + LOG_DIR+'/map.summary.xml ' \
	+ ' --fcd-output ' + LOG_DIR+ '/map.dump ' \
	+ ' --fcd-output.geo '\
	+ ' --ignore-route-errors '\
	+ ' --xml-validation never '\
	+ ' --verbose '
out = commands.getoutput(sim_cmd)
print(out)
