#!/usr/bin/env bash

# Get system name
system=$1


# Write to Runcommand Log
echo "RAINBOW" > $HOME/rainbow.txt

# Call my Python code and pass variable
sudo python /home/pi/rainbow.py &
