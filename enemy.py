from difflib import SequenceMatcher
from player import Player
import random


class Enemy:
    def __init__(self, damage):
        self._health = 100
        self._damage = damage
    




# Starts at random position, but can not start where an already existing enemy is, nor too close to the player.
# When button is clicked enough times to where the enemy has 0 HP remaining, delete button/object




#tekst1 = "TekstEn"
#tekst2 = "TekstTo"
#print(SequenceMatcher(None, tekst1, tekst2).ratio())