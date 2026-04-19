#Game Resource Classes

#Class for Weapon
class Weapon:
    def __init__(self,
                 name="",
                 size="s",
                 category="imprompt",
                 damage=1):
        self.name = name
        self.size = size
        self.category = category
        self.damage = damage


#Class for Game Entrant
class Entrant:
    def __init__(self,
                 weapon_instance,
                 name="",
                 intelligence=10,
                 speed=10,
                 strength=10,
                 armor_class=10):
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

    

    

    


        

