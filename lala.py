import pygame
from sense_hat import SenseHat
from pygame.locals import *

sense = SenseHat()

pygame.init()
pygame.display.set_mode((640,480))

class Player():
    def __init__(self):
        self.pseudo = "Graven"
        self.x = 0
        self.y = 7
        
    def get_pseudo(self):
        return self.pseudo
        
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    running = True
    player = Player("Vinetos")
    print("Bienvenue au joueur", player.get_pseudo())
    
        color = (229, 141, 41)
    player_x = player.get_x()
    player_y = player.get_y()
    sense.set_pixel(player_x, player_y, color)