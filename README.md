# retroblinkt
Scripts to make the Pimoroni Blinkt play nicely with RetroPie

Blinkt: https://shop.pimoroni.com/products/blinkt
RetroPie: https://retropie.org.uk/

As used in the 1963 Portable Retropie Console project:

Instructables:
Hackster:
Youtube:

The scripts assume a full Blinkt installation and a standard RetroPie installation on a Raspberry Pi.

There are five scripts here, three bash scripts that handle the logic of working with the RetroPie interface, and two Python scripts that control the Blinkt LED Strip. 

Bash Scripts
------------

These all need to be saved into folder:

/opt/retropie/configs/all/

autostart.sh

This script runs when RetroPie boots - usually it just contains a command to launch EmulationStation, but here we've added in a couple of others. Firstly it updates (or creates) a text file called rainbow.txt in the /home/pi/ directory. It populates the file with the single word "RAINBOW". It then launches the rainbow.py script, which displays cycling colours on the Blinkt - but only for as long as the word RAINBOW is present in the text file.

runcommand-onstart.sh

This script is fired when a game is selected, so on the launch of an emulator. First it updates the rainbow.txt file to the word "SOLID" (cancelling the cycling colours). then it runs the retroblinkt.py script, passing to it the name of the selected emulator as a parameter. 

runcommand-onend.sh

When you exit a game and the emulator closes, this script updates the rainbow.txt file back to "RAINBOW" and launches the rainbow.py script.

For more information on the usage of these scripts have a look at the RetroPie documentation:

https://github.com/RetroPie/RetroPie-Setup/wiki/runcommand#runcommand-onstart-and-runcommand-onend-scripts

Python Scripts
--------------

rainbow.py

This script lives in the /home/pi/ folder and is an exact copy of the rainbow.py script that comes with the downloaded examples when the Blinkt is fully installed. The only difference is that this copy of the script adds a condition to the While loop, so that instead of being infinite it is dependant on the presence of a specific text string in the rainbow.txt file - the word RAINBOW. 

retroblinkt.py

This script lives in /home/pi/Pimoroni/ (for no good reason) and controls the solid colour that is displayed once a game has been started. It accepts a parameter from the runcommand-onstart.sh script which is the name of the game system. It displays a different solid colour on the Blinkt depending on which platform name is passed in as a parameter. This script will only display while the word "SOLID" is present in rainbow.txt





