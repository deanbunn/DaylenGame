#!/usr/bin/env python3

#Import Required Modules
import game_resources
from game_utilities import log_game_data
from datetime import datetime
import uuid


#Default Method
def main():

    #Display Start Message
    print("Let's start the game! \n")

    #Var for Game Status
    gameStatus = ""

    #Var for Total Rounds
    totalRounds = 0

    #Create Entrant 1
    entrant1 = game_resources.Entrant(name="Raymond",strength=15)
    print(entrant1.showstats())

    #Create Entrant 2
    entrant2 = game_resources.Entrant(name="Daylen",speed=15,intelligence=20)
    print(entrant2.showstats())

    #Var for Game Unique GUID
    gameguid = str(uuid.uuid4())

    #Empty List for Game Data to Write to Log
    gamedata = []

    #While loop for entrants health
    while entrant1.health > 0 and entrant2.health > 0:

        #increment total rounds by 1
        totalRounds += 1

        #Rolling Attack Rolls for the round. Incrementing Wins or Health and Health Status
        if entrant1.attackroll() >= entrant2.attackroll():
            entrant1.wins += 1
            entrant2.health -= 5
            gamedata.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),gameguid,totalRounds,entrant1.name])
        else:
            entrant2.wins += 1
            entrant1.health -= 5
            gamedata.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),gameguid,totalRounds,entrant2.name])

        #Checking for Entrants Health
        if entrant1.health <= 0:
            gameStatus = entrant1.name + " lost the game!"

        if entrant2.health <= 0:
            gameStatus = entrant2.name + " lost the game!"
    

    #Logging Match Data
    log_game_data(gamedata)

    #reporting the outcome of the match
    print("Played a total of " + str(totalRounds) + " rounds!")
    print(entrant1.name + " won " + str(entrant1.wins) + " rounds" + " health is " + str(entrant1.health))
    print(entrant2.name + " won " + str(entrant2.wins) + " rounds" + " health is " + str(entrant2.health))
    print("\n")
    print(gameStatus)
    print("\n")


#Check to See If Script Ran Directly Instead of Imported
if __name__ == "__main__":
    main()

