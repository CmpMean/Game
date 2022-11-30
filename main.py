from player import Player
from enemy import Enemy
from world import World


def main():
    player = Player(1, "AVS")
    world = World(20, 20)
    
    # Temporary terminal input
    x = None
    while x != "":
        
        if x == "a":
            player.print_health()
        x = input("Press enter to exit ")
main()
    