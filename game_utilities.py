#Import Required Modules
import csv
import os
import json

def log_game_data(gamedata,logname="game-log.csv"):

    #Check If Game Log File Exists
    game_log_file_exists = os.path.isfile(logname)

    #Open Log File and Create It If Doesn't Exist
    with open(logname, mode='a', newline='') as file:
        writer = csv.writer(file)

        #If File Didn't Exist. Then Create CSV Header
        if not game_log_file_exists:
            writer.writerow(['timestamp',
                             'game id',
                             'round',
                             'entrant1 id',
                             'entrant1 name',
                             'entrant1 weapon',
                             'entrant1 damage',
                             'entrant2 id',
                             'entrant2 name',
                             'entrant2 weapon',
                             'entrant2 damage',
                             'winner id',
                             'winner name'])

        #Write Game Data to Log File
        writer.writerows(gamedata)






