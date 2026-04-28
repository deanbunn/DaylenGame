#!/usr/bin/env python3

'''
    Title: ruckchallenge.py
    Authors: Dean Bunn
    Last Edit: 2026-03-28
'''

#Import Challenge Resource Classes
import challenge_resources

#Default Method
def main():

    #Display Start Message
    print("Let's start the challege! \n")

    #Create Entrant 1
    entrant1 = challenge_resources.Entrant(name="Raymond",strength=25)
    print(entrant1.showstats())

    #Create Entrant 2
    entrant2 = challenge_resources.Entrant(name="Daylen",speed=15,intelligence=20)
    print(entrant2.showstats())

    #Round 1 
    if entrant1.attackroll() >= entrant2.attackroll():
        print(entrant1.name + " wins")
    else:
        print(entrant2.name + " wins")


#Check to See If Script Ran Directly Instead of Imported
if __name__ == "__main__":
    main()

