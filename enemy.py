from difflib import SequenceMatcher
from player import Player
import random
from random import randint
player = Player(3, "AVS")
class Enemy:
    def __init__(self, damage, name):
        self._health = 100 * self._heavy_set_generator()
        self._damage = damage
        self._name = name
        self._ID = randint(1, 20)
        self._x = self.position_x
        self._y = self.position_y

    def position_x(self):
        temp = randint(0, 300)
        if temp - player._position_x < 10:
            return (temp + 10)
        else: 
            return temp

    def position_y(self):
        temp = randint(0, 300)
        if temp - player._position_x < 10:
            return (temp + 10)
        else: 
            return temp

    def _heavy_set_generator(self):
        a = randint(1, 3)
        if a == 1:
            return 1.084
        if a == 2:
            return 1.12
        if a == 3:
            return 1.15

    def __str__(self):
        return self._name

    def __del__(self):
        self._die
    def _die(self):
        print(self._name)




# Starts at random position, but can not start where an already existing enemy is, nor too close to the player.
# When button is clicked enough times to where the enemy has 0 HP remaining, delete button/object




#tekst1 = "TekstEn"
#tekst2 = "TekstTo"
#print(SequenceMatcher(None, tekst1, tekst2).ratio())