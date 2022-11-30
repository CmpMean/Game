from difflib import SequenceMatcher
class Player:
    def __init__(self, heavy_set : int, weapon):
        self._health = 100
        self._status = "Alive"
        self._heavy_set = self.convert_heavy_set(heavy_set)
        self._kills_list = []
        self._medkits = 3
        self._kills = 0
        self._damage = self.damage_strength(weapon)
        self._positon_x = 20
        self._positon_y = 20
        self._damaged = 0

#####################################
# HEAVY SET RELATED
    def convert_heavy_set(self, heavy_set):
        if heavy_set == 0:
            return 1
        if heavy_set == 1:
            return 0.916
        if heavy_set == 2:
            return 0.88
        if heavy_set == 3:
            return 0.85

#####################################
# WEAPON RELATED
    def damage_strength(self, weapon):
        if weapon == "STG":
            return 37
        if weapon == "M2":
            return 36
        if weapon == "Garand":
            return 62
        if weapon == "AVS":
            return 37

#####################################
# HEALTH RELATED

    def update_health(self, damage_taken):
        self._health = self._health - (self._heavy_set * damage_taken)
        self._damaged += damage_taken
        if self._health <= 0:
            self._status = "Dead"
            #self._damaged += damage_taken

    def check_gameover(self):
        if self._status == "Dead":
            return True

    def print_health(self):
        print(f'Health remaining: {self._health}')

    def heal_medkit(self):
        if self._medkits > 0:
            self._health = 100
            self._medkits -= 1
            self._damaged = 0

    def return_medkits(self):
        return self._medkits

    def return_health(self):
        return self._health
    
    def return_damage_taken(self):
        return self._damaged
        
#####################################
# POSITIONS
    def move_back(self):
        if self._positon_y < 400:
            self._positon_y += 10
            return True
    def move_left(self):    
        if self._positon_x > 0:
            self._positon_x -= 1
            return True
    def move_forward(self):    
        if self._positon_y > 0:
            self._positon_y -= 1
            return True
    def move_right(self):    
        if self._positon_y < 400:
            self._positon_x += 1
            return True

    def valid_position_top(self):
        if self._positon_y > 0:
            return True
        else:
            return False

    def valid_position_left(self):
        if self._positon_x > 0:
            return True
        else:
            return False

    def valid_position_bottom(self):
        if self._positon_y < 400:
            return True
        else:
            return False

    def valid_position_right(self):
        if self._positon_x < 400:
            return True
        else:
            return False

    def print_position(self):
        print(f'x = {self._positon_x}, y = {self._positon_y}.')