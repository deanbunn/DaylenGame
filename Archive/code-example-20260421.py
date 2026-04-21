#!/usr/bin/env python3

#Import Required Modules
import game_resources
import game_utilities
from datetime import datetime
import uuid
import random
import time
import csv




#Default Method
def main():

    counts = {}

    with open('log_game_results.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            value = row['winner_name']
            counts[value] = counts.get(value,0) + 1
            
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for x in sorted_counts:
        print(x)

    


















#Check to See If Script Ran Directly Instead of Imported
if __name__ == "__main__":
    main()