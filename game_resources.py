#Game Resource Classes and Functions

#Import Required Modules
import json
import random

#Class for Weapon
class Weapon:
    def __init__(self,
                 id=0,
                 name="",
                 size="s",
                 category="imprompt",
                 damage=1):
        self.id = id
        self.name = name
        self.size = size
        self.category = category
        self.damage = damage


#Class for Game Entrant
class Entrant:
    def __init__(self,
                 weapon_instance,
                 id=0,
                 name="",
                 intelligence=10,
                 speed=10,
                 strength=10,
                 armor_class=10):
        self.id = id
        self.name = name
        self.intelligence = intelligence
        self.speed = speed
        self.strength = strength
        self.armor_class = armor_class
        self.wins = 0
        self.health = 100
        self.attacks_per_round = 1
        self.weapon = weapon_instance
        
        #Determine Attacks Per Round
        if self.speed + self.strength + self.intelligence >= 40:
            self.attacks_per_round = 3
        elif self.speed + self.strength + self.intelligence >= 30:
            self.attacks_per_round = 2
        

    def showstats(self):
        return f"\nName: {self.name} \nIntelligence: {self.intelligence} \nSpeed: {self.speed} \nStrength: {self.strength} \nArmour Class: {self.armor_class} \nWeapon: {self.weapon.category} \nAttacks Per Round: {self.attacks_per_round} \n"



#Function for Retrieving Weapon Listing from Resource Json File
def get_weapon_listing():

    #List for Weapon Objects
    weaponlisting = []

    #Load Weapons Json File and Use Data to Create Weapon Objects
    with open("resource_weapons.json") as f:
        weapons_json = json.load(f)

        for wpn in weapons_json:
            nwwpn = Weapon(id=wpn["id"],
                           name=wpn["name"],
                           category=wpn["category"],
                           size=wpn["size"],
                           damage=wpn["damage"])
            
            #Add Weapon to Weapon Listing
            weaponlisting.append(nwwpn)

    return weaponlisting
    

#Function for Retrieving Entrants Listing from Resource Json File
def get_entrants_listing():

    #List for Entrant Objects
    entrantlisting = []

    #Pull Weapons List
    weapons = get_weapon_listing()

    #Load Entrants Json File and Use Data to Create Entrant Objects
    with open("resource_entrants.json") as f:
        entrants_json = json.load(f)

        for etrt in entrants_json:
            nwetrnt = Entrant(id=etrt["id"],
                              name=etrt["name"],
                              intelligence=etrt["intelligence"],
                              speed=etrt["speed"],
                              strength=etrt["strength"],
                              armor_class=etrt["armor_class"],
                              weapon_instance=weapons[random.randint(0,len(weapons) -1)]
                              )

            #Add Entrant to Listing
            entrantlisting.append(nwetrnt)

    return entrantlisting




    

