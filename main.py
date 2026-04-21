#!/usr/bin/env python3

#Import Required Modules
import game_resources
import game_utilities
from datetime import datetime
import uuid
import random
import time


#Default Method
def main():

    #Var for Total Rounds
    total_rounds = 0

    #Var for Game Unique GUID
    game_guid = str(uuid.uuid4())

    #Vars for Game Winners
    game_winner_id = 0
    game_winner_name = ""

    #Empty List for Game Data to Write to Log
    game_data = []

    #Empty List for Round Data to Write to Log
    round_data = []

    #List of Conflict Sounds
    conflict_sounds = game_utilities.load_conflict_sounds()

    #List for Entrants
    entrants = game_resources.get_entrants_listing()

    #Randomly Determine the Two Entrants
    entrant1 = entrants[random.randint(0,len(entrants) -1)]
    entrant2 = entrants[random.randint(0,len(entrants) -1)]

    #Ensure Duplicate Entrants Are Not Selected
    while entrant1.id == entrant2.id:
        entrant2 = entrants[random.randint(0,len(entrants) -1)]


    #Display Start Message
    print("\nThe Match Contestants:")

    #Show Entrants Stats
    print(entrant1.showstats())
    print("vs.")
    print(entrant2.showstats())

    #Pause Script for Match Realism
    time.sleep(1.0)

    #Display Start Message
    print("Let's get ready to rumble!\n")

    #Pause Script for Match Realism
    time.sleep(0.5)

    #While loop for entrants health
    while entrant1.health > 0 and entrant2.health > 0:

        #Increment total rounds by 1
        total_rounds += 1

        #Pause Script for Match Realism
        time.sleep(0.25)

        #Var for Conflict Sound
        round_sound = ""

        #Dynamically Configure Round Sound
        for s in range(5):
            round_sound += conflict_sounds[random.randint(0,len(conflict_sounds) -1)] + " "
        

        #Display Round Sound
        print(round_sound)

        #Vars for Round Winner
        round_winner = ""
        round_winner_id = 0

        #Var for Entrant 1 Per Round Damage
        ent1_per_rnd_damage = 0

        #Var for Entrant 2 Per Round Damage
        ent2_per_rnd_damage = 0

        #Determine Entrant 1 Attack Roles
        for ent1 in range(entrant1.attacks_per_round):
            #Var for Random Attack Role
            if random.randint(1,20) >= entrant2.armor.defense:
                ent1_per_rnd_damage += random.randint(1,entrant1.weapon.damage)


        #Determine Entrant 2 Attack Roles
        for ent2 in range(entrant2.attacks_per_round):
            #Var for Random Attack Role
            if random.randint(1,20) >= entrant1.armor.defense:
                ent2_per_rnd_damage += random.randint(1,entrant2.weapon.damage)

        
        #Apply Round Damage to Entrants
        entrant1.health -= ent2_per_rnd_damage
        entrant2.health -= ent1_per_rnd_damage


        #Comparing Damage for the round. Incrementing Wins or Health and Health Status
        if ent1_per_rnd_damage >= ent2_per_rnd_damage:
            entrant1.wins += 1
            round_winner = entrant1.name
            round_winner_id = entrant1.id
        else:
            entrant2.wins += 1
            round_winner = entrant2.name
            round_winner_id = entrant2.id
            
        
        #Add to Round Log Virtual Data
        round_data.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          game_guid,
                          total_rounds,
                          entrant1.id,
                          entrant1.name,
                          entrant1.armor.name,
                          entrant1.weapon.category,
                          ent1_per_rnd_damage,
                          entrant2.id,
                          entrant2.name,
                          entrant2.armor.name,
                          entrant2.weapon.category,
                          ent2_per_rnd_damage,
                          round_winner_id,
                          round_winner])

        
    #Logging Match Data
    game_utilities.log_round_data(round_data)

    #Reporting the outcome of the match
    print("\nContest lasted a total of " + str(total_rounds) + " rounds!")
    print(entrant1.name + " won " + str(entrant1.wins) + " rounds." + " Health status at " + str(entrant1.health))
    print(entrant2.name + " won " + str(entrant2.wins) + " rounds." + " Health status at " + str(entrant2.health) + "\n")
    
    #Display Winner's Name and Weapon Name
    if entrant1.health >= entrant2.health:
        print(entrant1.name + " was victorious using \"" + entrant1.weapon.name + "\" " + entrant1.weapon.category + "\n")
        game_winner_id = entrant1.id
        game_winner_name = entrant1.name
    else:
        print(entrant2.name + " was victorious using \"" + entrant2.weapon.name + "\" " + entrant2.weapon.category + "\n")
        game_winner_id = entrant2.id
        game_winner_name = entrant2.name


    #Add to Game Log Virtual Data
    game_data.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                      game_guid,
                      entrant1.id,
                      entrant1.name,
                      entrant1.armor.name,
                      entrant1.weapon.category,
                      entrant1.health,
                      entrant1.wins,
                      entrant2.id,
                      entrant2.name,
                      entrant2.armor.name,
                      entrant2.weapon.category,
                      entrant2.health,
                      entrant2.wins,
                      game_winner_id,
                      game_winner_name])
    
    #Logging Game Data
    game_utilities.log_game_data(game_data)

    #Pull Game Wins
    leader_board = game_utilities.count_game_wins()

    #Display Leader Board
    print("=" * 40)
    print("Leader Board")
    print("=" * 40)
    print(f"{'Rank':<5} {'Name':<18} {'Wins':<5}")
    print("-" * 40)
    for i,(key,value) in enumerate(leader_board, start=1):
        print(f"{i:<5} {key:<18} {value:<5}")
    
    print("\n")


#Check to See If Script Ran Directly Instead of Imported
if __name__ == "__main__":
    main()

