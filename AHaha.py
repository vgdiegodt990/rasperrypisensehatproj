import pygame
from sense_hat import SenseHat
from pygame.locals import *
from random import randint
import random

sense = SenseHat()

r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
color = (r,g,b)

pygame.init()
pygame.display.set_mode((640,480))

class Player():
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.x = 0
        self.y = 7
        
    def get_pseudo(self):
        return self.pseudo
    
    def move_left(self):
        self.x -= 1
        
    def move_right(self):
        self.x += 1
    
    def move_up(self):
        self.y -= 1
        
    def move_down(self):
        self.y += 1
        
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Objective():
    def __init__(self):
        self.x = randint(0, 7)
        self.y = randint(0, 7)
        
    def random_place(self):
        self.x = randint(0, 7)
        self.y = randint(0, 7)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def check_capture(self, player):
        return player.get_x() == self.x and player.get_y() == self.y
    
running = True
player = Player("Vinetos")
objective = Objective()
points = 0
print("Bienvenue au joueur", player.get_pseudo())

sense.clear()

obj_color = (140, 140, 140)
sense.set_pixel(objective.get_x(), objective.get_y(), obj_color)

color = (229, 141, 41)
player_x = player.get_x()
player_y = player.get_y()
sense.set_pixel(player_x, player_y, color)
    
while running is True:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            print("Bye bye!")
        elif event.type == KEYDOWN:
                
            if event.key == K_LEFT and player.get_x() > 0:
                print("Left")
                player.move_left()
            elif event.key == K_RIGHT and player.get_x() < 7:
                print("Right")
                player.move_right()
            elif event.key == K_UP and player.get_y() > 0:
                print("Up")
                player.move_up()
            elif event.key == K_DOWN and player.get_y() < 7:
                print("Down")
                player.move_down()
                
            if objective.check_capture(player):
                print("Captured!")
                objective.random_place()
                points += 1
                if points >= 3:
                    print("Victory")
                    sense.clear()
                    sense.show_message("Nice!", back_colour=color, scroll_speed=0.05)
                    points = 0
                
            sense.clear() 
            sense.set_pixel(player.get_x(),player.get_y(), color)
            sense.set_pixel(objective.get_x(), objective.get_y(), obj_color)