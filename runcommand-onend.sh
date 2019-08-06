#!/usr/bin/env bash

# Write RAINBOW to the text file
echo "RAINBOW" > $HOME/rainbow.txt

# Call the Python code to run the rainbow colours
sudo python /home/pi/rainbow.py &
