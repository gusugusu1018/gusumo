# Environment
* ubuntu16.04
* sumo-1.1.0

# Setup
if you use bash
```
echo "export SUMO_HOME=/usr/share/sumo" >> ~/.bashrc
source ~/.bashrc
```

# How to use
## make grid map
```
./gridnetgen.sh
```

## run simple simulation
```
./runner.py gridmap
# or
./runner.sh gridmap
```

## plot net speed
```
./plot_net_speed.sh
```
