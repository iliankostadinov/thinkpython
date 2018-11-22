#!/usr/bin/python3

import math

#Practice using Python as calculator

if __name__ == '__main__':

    #Print volume of a sphere with radius 5
    print("The volume of a sphere with radius 5 is", 4.0/3.0*math.pi*5.0**3)

    #Calculate wholesale prise for 60 copies
    print("Wholesale prise for 60 copies is", 24.0*0.4*60+3.0+59.0*0.75)

    #Calculate when I get home
    seconds = 2*(8*60+15)+3*(7*60+12)
    minutes = seconds/60.0
    print("I arrived at 7 and", int(minutes-8), "minutes")

