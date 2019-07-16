#!/usr/bin/env bash

# Get system name
system=$1


# Write to Runcommand Log
echo "SOLID" > $HOME/rainbow.txt

#sudo python /home/pi/rainbow.py &

# Call my Python code and pass variable
sudo python /home/pi/Pimoroni/retroblinkt.py $system &
