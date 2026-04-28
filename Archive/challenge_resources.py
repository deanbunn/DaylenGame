#!/usr/bin/env python3

import random

#Class for Challenge Entrant
class Entrant:
    def __init__(self,name="",intelligence=10,speed=10,strength=5):
        self.name = name
        self.intelligence = intelligence
        self.speed = speed
        self.strength = strength

    def showstats(self):
        return f"Name: {self.name} \nIntelligence: {self.intelligence} \nSpeed: {self.speed} \nStrength: {self.strength} \n\n"

    def attackroll(self):
        return self.intelligence + self.speed + self.strength + random.randint(1,50)
    


        

