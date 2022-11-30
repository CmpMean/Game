from player import Player
from enemy import Enemy
from tkinter import *
from random import randint
from datetime import datetime, timedelta


ini_time_for_now = datetime.now()


root = Tk()
root.title("Game Test")
#root.iconbitmap("C:\Users\CmpMean\Coding\icon.ico")
#root.geometry("400x400")
img = PhotoImage(file="bee.png")
img2 = PhotoImage(file="enemy_icon.png")
player = Player(3, "AVS")
enemies = []
ge_names = open("german_names.txt")
for line in ge_names:
    line = line.rstrip().split()   
    enemies.append(Enemy(randint(10, 30), line))

class World:
    def __init__(self, master, widthx, heighty):
        self._health = player.return_health()
        #interface = Canvas(master, bg="light blue")
        #interface.pack()
        self._canvas = Canvas(master, width=widthx, height=heighty, bg="light blue")
        self._canvas.pack()


        #self._playerModel = Canvas(master)
        #self._playerModel.pack()

        #self._playerID = self._canvas.create_oval(0, 0, 10, 10, width=3)
        self._playerID = self._canvas.create_image(0, 0, anchor=NW, image=img)
        #self._healthbar.pack()
        self._rectangleID_red = self._canvas.create_rectangle(300, 170, 320, 270, fill="red")
        self._rectangleID = self._canvas.create_rectangle(320, 270, 300, 170, fill="green")

        
        ############ 
        # MOVEMENT
        self._button_w = Button(self._canvas, text="W", command=self.w)
        self._button_w.pack(pady=20)
        self._button_w.place(x= 97, y=93)

        self._button_a = Button(self._canvas, text="A", command=self.a)
        self._button_a.pack(pady=20)
        self._button_a.place(x= 80, y=120)

        self._button_s = Button(self._canvas, text="S", command=self.s)
        self._button_s.pack(pady=20)
        self._button_s.place(x= 100, y=120)

        self._button_d = Button(self._canvas, text="D", command=self.d)
        self._button_d.pack(pady=20)
        self._button_d.place(x= 117, y=120)
        ##############
        # Manual check
        self._button_check = Button(self._canvas, text="Find Player Position", command=self.check)
        self._button_check.pack(pady=20)
        self._button_check.place(x = 160, y=160)


        self._button_alive = Button(self._canvas, text="Take damage", command=self.take_damage)
        self._button_alive.pack(pady=20)
        self._button_alive.place(x= 110, y=110)

        
        #############
        # HEALING


        #self._heal = Button(self._canvas, text=f'Heal', command=self.heal)
        self._heal = Button(self._canvas, text=f'Heal {player.return_medkits()}', command=self.heal)
        self._heal.pack()
        self._heal.place(x=300, y=300)
        x = 0
        for object in enemies:
            
            if object._ID == randint(1, 20):
                self._enemy = self._canvas.create_image(9+(x*2), 9, anchor=NW, image=img2)
                x += 9
        #############
        # FIRING
        
        #

    def w(self):
        player.move_forward()
        if player.valid_position_top() == True:
            self._canvas.move(self._playerID, 0, -1)

    def a(self):
        player.move_left()
        if player.valid_position_left() == True:
            self._canvas.move(self._playerID, -1, 0)
    def s(self):
        player.move_back()
        if player.valid_position_bottom() == True:
            self._canvas.move(self._playerID, 0, +10)
    def d(self):
        player.move_right()
        if player.valid_position_right() == True:
            self._canvas.move(self._playerID, 1, 0)

    def check(self):
        player.print_position()
    
    def take_damage(self):
        player.update_health(20)
        
        if player.check_gameover() == True:
            print("Game Over")
            root.destroy()
        if player.check_gameover() == False:
            self.update_healthbar()

    def heal(self):
        player.heal_medkit()
        self.update_healthbar()
        self._heal.forget
        self._heal = Button(self._canvas, text=f'Heal {player.return_medkits()}', command=self.heal)
        self._heal.pack()
        self._heal.place(x=300, y=300)
    
    def update_healthbar(self):
        #self._canvas
        self._canvas.delete(self._rectangleID)
        self._rectangleID = self._canvas.create_rectangle(320, 270, 300, 170+player._damaged, fill="green")

world = World(root, 400, 400)
    



    #    self._map = self._make_map()  # Kaller på metoden for å lage rutenett
    #def _make_map(self):
    #    test2 = []
    #    for x in range(self._rows):
    #        test2.append(self._make_row())   # Bruker neste metode for å fylle in rader basert på kolonner.
    #    return test2    # Returnerer listen

    #def _make_row(self):
    #    test = []        
    #    for x in range(self._columns):
    #        test.append(None)
    #    return test     # Returnerer listen


root.mainloop()