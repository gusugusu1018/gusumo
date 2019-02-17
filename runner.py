#!/usr/bin/env python

# @file		runner.py
# @author	Yuji Ogusu
# @date		2019-02-16

import argparse
import subprocess
import sys
import os
import datetime

## Get SUMO Environment information
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

## Set Simulation Environment
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MAP_DIR=os.path.join(BASE_PATH,str(args.mapdirectory))
NET_FILE=MAP_DIR+'/map.net.xml'
TRIPS_FILE=MAP_DIR+'/map.trips.xml'
ROUTE_FILE=MAP_DIR+'/map.rou.xml'
now = datetime.datetime.now()
LOG_DIR=os.path.join(MAP_DIR,"log",now.strftime("%Y%m%d-%H%M%S"))

## Show infomation
print('script          : '+__file__)
print('base            : '+BASE_PATH)
print('sumo home       : '+SUMO_PATH)
print('bin path        : '+BIN_PATH)
print('tools path      : '+TOOLS_PATH)
print('using directory : '+MAP_DIR) 
print('use CUI         : '+str(args.cui))
print('end time        : '+str(args.endtime))
print('net file        : '+NET_FILE)
print('trips file      : '+TRIPS_FILE)
print('route file      : '+ROUTE_FILE)
print('log files       : '+LOG_DIR)

## Generate Trips Using srandomTrips.py in sumo-tools
print("\033[36mGenerate trips\033[0m")

try:
	out = subprocess.check_output([ \
		os.path.join(TOOLS_PATH , 'randomTrips.py') \
		, '--net-file' , NET_FILE \
		, '--output-trip-file' , TRIPS_FILE \
		, '--verbose'])
except subprocess.CalledProcessError as e:
	sys.exit('FAILED : ' + e.cmd)

## Generate route Using duarouter in sumo
print("\033[36mGenerate route\033[0m")

try:
	out = subprocess.check_output([ \
		os.path.join(BIN_PATH,'duarouter') \
		, '--route-files' , TRIPS_FILE \
		, '--net-file' , NET_FILE \
		, '--output-file' , ROUTE_FILE \
		, '--ignore-errors' \
		, '--xml-validation','never'])
	print(out)
except subprocess.CalledProcessError as e:
	sys.exit('FAILED : ' + e.cmd)

## Start SUMO 
print("\033[36mStart simulation\033[0m")
os.makedirs(LOG_DIR)
print("make Directory for log : "+LOG_DIR)

SUMO_CMD='sumo-gui'
if args.cui :
	SUMO_CMD='sumo'

try:
	out = subprocess.check_output([ \
		os.path.join(BIN_PATH,SUMO_CMD) \
		, '--begin','0','--end',args.endtime \
		, '--net-file' , NET_FILE \
		, '--route-files' , ROUTE_FILE \
		, '--summary-output' , LOG_DIR+'/map.summary.xml' \
		, '--fcd-output' , LOG_DIR+'/map.dump' \
		, '--fcd-output.geo'\
		, '--ignore-route-errors'\
		, '--xml-validation','never'\
		, '--verbose'])
	print(out)
except subprocess.CalledProcessError as e:
	sys.exit('FAILED : ' + e.cmd)
