#!/usr/bin/env python3

#Import Game Resource Classes
import game_resources

#Default Method
def main():

    #Display Start Message
    print("Let's start the game! \n")

    #Create Entrant 1
    entrant1 = game_resources.Entrant(name="Raymond",strength=15)
    print(entrant1.showstats())

    #Create Entrant 2
    entrant2 = game_resources.Entrant(name="Daylen",speed=15,intelligence=20)
    print(entrant2.showstats())

    for i in range(1,11):
        if entrant1.attackroll() >= entrant2.attackroll():
            entrant1.wins += 1
            entrant2.health -= 5
        else:
            entrant2.wins += 1
            entrant1.health -= 5

    
    print(entrant1.name + " won " + str(entrant1.wins) + " matches ")
    print(entrant1.name + " health is " + str(entrant1.health))
    print(entrant2.name + " won " + str(entrant2.wins) + " matches ")
    print(entrant2.name + " health is " + str(entrant2.health))


#Check to See If Script Ran Directly Instead of Imported
if __name__ == "__main__":
    main()

