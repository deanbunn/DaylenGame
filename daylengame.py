#!/usr/bin/env python3

#Import Required Modules
import game_resources
from game_utilities import log_game_data
from datetime import datetime
import uuid
import random


#Default Method
def main():

    #Display Start Message
    print("Let's start the game! \n")

    #Var for Game Status
    gameStatus = ""

    #Var for Total Rounds
    totalRounds = 0

    #########################
    # Initiate Game Weapons
    #########################

    #Create Weapon 1
    Piano = game_resources.Weapon(name="Grand Dad",
                                    size="l",
                                    damage=25)
    
    #Create Weapon 2
    Dagger = game_resources.Weapon(name="I am the Spy!",
                                    size="s",
                                    damage=5)
    
    #Create Weapon 3
    Club =  game_resources.Weapon(name="Unga and Bunga",
                                  size="s",
                                  damage=5)
    
    #Create Weapon 4
    Shortsword = game_resources.Weapon(name="The Inbetween",
                                       size="m",
                                       damage=10)
    
    #Create Weapon 5
    Greatsword = game_resources.Weapon(name="The Dark Souls",
                                       size="l",
                                       damage=15)

    ##########################
    # Initiate Game Entrants
    ##########################

    #Create Entrant 1
    entrant1 = game_resources.Entrant(name="Raymond",
                                      strength=15,
                                      weapon_instance=Dagger)
    
    print(entrant1.showstats())

    #Create Entrant 2
    entrant2 = game_resources.Entrant(name="Daylen",
                                      speed=15,
                                      intelligence=20,
                                      weapon_instance=Greatsword)
    
    print(entrant2.showstats())

    #######################
    # Starting the Match
    #######################

    #Var for Game Unique GUID
    gameguid = str(uuid.uuid4())

    #Empty List for Game Data to Write to Log
    gamedata = []

    #While loop for entrants health
    while entrant1.health > 0 and entrant2.health > 0:

        #Increment total rounds by 1
        totalRounds += 1

        #Var for Round Winner
        roundWinner = ""

        #Var for Entrant 1 Per Round Damage
        ent1PerRndDamage = 0

        #Var for Entrant 2 Per Round Damage
        ent2PerRndDamage = 0

        #Determine Entrant 1 Attack Roles
        for ent1 in range(entrant1.attacks_per_round):
            #Var for Random Attack Role
            if random.randint(1,20) >= entrant2.armor_class:
                ent1PerRndDamage += random.randint(1,entrant1.weapon.damage)


        #Determine Entrant 2 Attack Roles
        for ent2 in range(entrant2.attacks_per_round):
            #Var for Random Attack Role
            if random.randint(1,20) >= entrant1.armor_class:
                ent2PerRndDamage += random.randint(1,entrant2.weapon.damage)


        #Comparing Damage for the round. Incrementing Wins or Health and Health Status
        if ent1PerRndDamage >= ent2PerRndDamage:
            entrant1.wins += 1
            entrant2.health -= ent1PerRndDamage
            roundWinner = entrant1.name
        else:
            entrant2.wins += 1
            entrant1.health -= ent2PerRndDamage
            roundWinner = entrant2.name
            
        
        #Add to Log Virtual Data
        gamedata.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        gameguid,
                        totalRounds,
                        ent1PerRndDamage,
                        ent2PerRndDamage,
                        roundWinner])

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

