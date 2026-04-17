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
    game_status = ""

    #Var for Total Rounds
    total_rounds = 0

    #List for Weapons
    weapons = []

    #List for Entrants
    entrants = []

    #########################
    # Initiate Game Weapons
    #########################

    #Initiate Piano
    piano = game_resources.Weapon(name="Grand Dad",
                                  category="Piano",
                                  size="l",
                                  damage=25)
    
    #Initiate Dagger
    dagger = game_resources.Weapon(name="I am the Spy!",
                                   category="Dagger",
                                   size="s",
                                   damage=5)
    
    #Initiate Club
    club =  game_resources.Weapon(name="Unga and Bunga",
                                  category="Club",
                                  size="s",
                                  damage=5)
    
    #Initiate Shortsword 
    shortsword = game_resources.Weapon(name="The Inbetween",
                                       category="Shortsword",
                                       size="m",
                                       damage=10)
    
    #Initiate Greatsword
    greatsword = game_resources.Weapon(name="The Dark Souls",
                                       category="Greatsword",
                                       size="l",
                                       damage=15)
    
    #Load Weapons List
    weapons.append(piano)
    weapons.append(dagger)
    weapons.append(club)
    weapons.append(shortsword)
    weapons.append(greatsword)

    ##########################
    # Initiate Game Entrants
    ##########################

    #Initiate Raymond
    raymond = game_resources.Entrant(name="Raymond",
                                     strength=15,
                                     weapon_instance=weapons[random.randint(0,len(weapons) -1)])

    #Initiate Daylen
    daylen = game_resources.Entrant(name="Daylen",
                                    speed=15,
                                    intelligence=20,
                                    weapon_instance=weapons[random.randint(0,len(weapons) -1)])

    #Initiate Juan
    juan = game_resources.Entrant(name="Juan",
                                  speed=12,
                                  strength=15,
                                  weapon_instance=weapons[random.randint(0,len(weapons) -1)])
    
    #Initiate Charlie 
    charlie = game_resources.Entrant(name="Charlie",
                                     speed=14,
                                     intelligence=15,
                                     weapon_instance=weapons[random.randint(0,len(weapons) -1)])

    #Load Entrants List
    entrants.append(raymond)
    entrants.append(daylen)
    entrants.append(juan)
    entrants.append(charlie)

    #Randomly Determine the Two Entrants
    entrant1 = entrants[random.randint(0,len(entrants) -1)]
    entrant2 = entrants[random.randint(0,len(entrants) -1)]

    #Ensure Duplicate Entrants Are Not Selected
    while entrant1.name == entrant2.name:
        entrant2 = entrants[random.randint(0,len(entrants) -1)]


    #Show Entrants Stats
    print(entrant1.showstats())
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
        total_rounds += 1

        #Var for Round Winner
        round_winner = ""

        #Var for Entrant 1 Per Round Damage
        ent1_per_rnd_damage = 0

        #Var for Entrant 2 Per Round Damage
        ent2_per_rnd_damage = 0

        #Determine Entrant 1 Attack Roles
        for ent1 in range(entrant1.attacks_per_round):
            #Var for Random Attack Role
            if random.randint(1,20) >= entrant2.armor_class:
                ent1_per_rnd_damage += random.randint(1,entrant1.weapon.damage)


        #Determine Entrant 2 Attack Roles
        for ent2 in range(entrant2.attacks_per_round):
            #Var for Random Attack Role
            if random.randint(1,20) >= entrant1.armor_class:
                ent2_per_rnd_damage += random.randint(1,entrant2.weapon.damage)


        #Comparing Damage for the round. Incrementing Wins or Health and Health Status
        if ent1_per_rnd_damage >= ent2_per_rnd_damage:
            entrant1.wins += 1
            entrant2.health -= ent1_per_rnd_damage
            round_winner = entrant1.name
        else:
            entrant2.wins += 1
            entrant1.health -= ent2_per_rnd_damage
            round_winner = entrant2.name
            
        
        #Add to Log Virtual Data
        gamedata.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        gameguid,
                        total_rounds,
                        entrant1.weapon.category,
                        ent1_per_rnd_damage,
                        entrant2.weapon.category,
                        ent2_per_rnd_damage,
                        round_winner])

        #Checking for Entrants Health
        if entrant1.health <= 0:
            game_status = entrant1.name + " lost the game!"

        if entrant2.health <= 0:
            game_status = entrant2.name + " lost the game!"
    

    #Logging Match Data
    log_game_data(gamedata)

    #reporting the outcome of the match
    print("Played a total of " + str(total_rounds) + " rounds!")
    print(entrant1.name + " won " + str(entrant1.wins) + " rounds" + " health is " + str(entrant1.health))
    print(entrant2.name + " won " + str(entrant2.wins) + " rounds" + " health is " + str(entrant2.health))
    print("\n")
    print(game_status)
    print("\n")
    


#Check to See If Script Ran Directly Instead of Imported
if __name__ == "__main__":
    main()

