#Game Resource Classes

#Class for Weapon
class Weapon:
    def __init__(self,
                 name="",
                 size="s",
                 damage=1):
        self.name = name
        self.size = size
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
        self.health = 75
        self.attacks_per_round = 1
        self.weapon = weapon_instance
        
        #Determine Attacks Per Round
        if self.speed + self.strength + self.intelligence >= 30:
            self.attacks_per_round = 3
        elif self.speed + self.strength + self.intelligence >= 20:
            self.attacks_per_round = 2
        

    def showstats(self):
        return f"Name: {self.name} \nIntelligence: {self.intelligence} \nSpeed: {self.speed} \nStrength: {self.strength} \n\n"

    

    

    


        

