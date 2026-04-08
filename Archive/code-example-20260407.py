#!/usr/bin/env python3

#Import Specific Functions from a Module
from game_utilities import log_game_data
from datetime import datetime
import uuid

#Var for Game Unique GUID
gameguid = str(uuid.uuid4())

#Empty List for Game Data to Write to Log
gamedata = []

for i in range(1,6):
    #Add Item to GameData List. #For More Specific Timestamp use datetime.now().isoformat()
    gamedata.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),gameguid,i,"nobody"])
    

log_game_data(gamedata)


