#!/usr/bin/env python3

#Import Required Modules
import game_resources
from game_utilities import log_game_data
from datetime import datetime
import uuid
import random

#Default Method
def main():
    
    weaponslist = []

    greatsword = game_resources.Weapon(name="The Dark Souls",
                                       size="l",
                                       damage=15)
    
    shortsword = game_resources.Weapon(name="The Inbetween",
                                       size="m",
                                       damage=10)
    
    club =  game_resources.Weapon(name="Unga and Bunga",
                                  size="s",
                                  damage=5)
    
    weaponslist.append(greatsword)
    weaponslist.append(shortsword)
    weaponslist.append(club)


    testing = weaponslist[random.randint(0,len(weaponslist) -1)]

    print(testing.name)




#Check to See If Script Ran Directly Instead of Imported
if __name__ == "__main__":
    main()


