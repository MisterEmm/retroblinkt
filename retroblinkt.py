import sys
from blinkt import set_clear_on_exit, set_all, set_pixel,show,set_brightness
from time import sleep

def red():

    set_all(255,0,0)
    set_brightness(0.5)
    show()

def green():

    set_all(0,128,0)
    set_brightness(0.5)
    show()

def purple():

    set_all(255,0,255)
    set_brightness(0.5)
    show()

def yellow():

    set_all(255,255,0)
    set_brightness(0.5)
    show()

def orange():
    set_all(255,165,0)
    set_brightness(0.5)
    show()

platform = sys.argv[1]
#print platform
#print len(platform)

while 'SOLID' in open('/home/pi/rainbow.txt').read():

    if platform == "nes":
        green()
    elif platform == "snes":
        yellow()
    elif platform == "atari2600":
        orange()
    elif platform == "psx":
        red()
    elif platform == "megadrive":
        purple()
    else:
        purple()
        print("Unknown Console")

set_all(0,0,0)
show()
