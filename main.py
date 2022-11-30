#from player import Player
from enemy import Enemy
#from world2 import World


def main():
    player = Player(1, "AVS")
    world = World(20, 20)
    
    # Temporary terminal input
    x = None
    while x != "":
        
        if x == "a":
            player.print_health()
        x = input("Press enter to exit ")
#main()

def test():
    enemy1 = Enemy(40, "Robert")
    print(enemy1)
    enemy1.__del__

test()
    