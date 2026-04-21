#Import Required Modules
import csv
import os
import json


def log_round_data(rounddata,logname="log_round_results.csv"):

    #Check If Round Log File Exists
    round_log_file_exists = os.path.isfile(logname)

    #Open Log File and Create It If Doesn't Exist
    with open(logname, mode='a', newline='') as file:
        writer = csv.writer(file)

        #If File Didn't Exist. Then Create CSV Header
        if not round_log_file_exists:
            writer.writerow(['timestamp',
                             'game_id',
                             'round',
                             'entrant1_id',
                             'entrant1_name',
                             'entrant1_armor',
                             'entrant1_weapon',
                             'entrant1_damage',
                             'entrant2_id',
                             'entrant2_name',
                             'entrant2_armor',
                             'entrant2_weapon',
                             'entrant2_damage',
                             'winner_id',
                             'winner_name'])

        #Write Round Data to Log File
        writer.writerows(rounddata)



def log_game_data(gamedata,logname="log_game_results.csv"):

    #Check If Game Log File Exists
    game_log_file_exists = os.path.isfile(logname)

    #Open Log File and Create It If Doesn't Exist
    with open(logname, mode='a', newline='') as file:
        writer = csv.writer(file)

        #If File Didn't Exist. Then Create CSV Header
        if not game_log_file_exists:
            writer.writerow(['timestamp',
                             'game_id',
                             'entrant1_id',
                             'entrant1_name',
                             'entrant1_armor',
                             'entrant1_weapon',
                             'entrant1_health',
                             'entrant1_rounds_won',
                             'entrant2_id',
                             'entrant2_name',
                             'entrant2_armor',
                             'entrant2_weapon',
                             'entrant2_health',
                             'entrant2_rounds_won',
                             'winner_id',
                             'winner_name'])

        #Write Game Data to Log File
        writer.writerows(gamedata)


def load_conflict_sounds(soundsfile="utility_conflict_sounds.txt"):
    
    #List to Return
    conflictsounds = []

    with open(soundsfile,"r") as f:
        for line in f:
            conflictsounds.append(line.strip())

    
    return conflictsounds


def count_game_wins(logname="log_game_results.csv"):
    
    #Dict to Return
    sorted_counts = {}

    #Dict for Parsing
    counts = {}

    #Parse Through CSV File and Load Dict Based Upon Winner Name and Number of Appearences
    with open(logname,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            value = row['winner_name']
            counts[value] = counts.get(value,0) + 1

    #Sort the Counts by the Second Value
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_counts

