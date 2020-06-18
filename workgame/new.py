import sys
import pygame
from pygame.locals import QUIT
from pygame.locals import *

def main():
    pygame.init()
    win = pygame.display.set_mode((800,600))
    pygame.display.set_caption('blackbear saved polarbear')
    win.fill((0, 0, 0))

    head_font = pygame.font.SysFont(None, 60)
    head_surface = head_font.render('blackbear saved polarbear', True, (255, 255, 255))
    win.blit(head_surface, (130, 250))
    pygame.display.update()
    pygame.time.wait(2000)
  
    win.fill((255, 255, 255))   
    round_surface = head_font.render('Round1', True, (0, 0, 0))  
    win.blit(round_surface, (300, 250))   
    pygame.display.update()  
    pygame.time.wait(1000)
    round = 1
    good = 0
    life = True
    deadthing = 0
  
    cake = []
    cake_box = []
    cake_name = ["resources/png/blackbear1.png", "resources/png/ice.png", "resources/png/donuts.png", "resources/png/macaron.png", "resources/png/cake.png", "resources/png/blackbear2.png"]
    
    for i in range(6):
        cake[i] = pygame.image.load(cake_name)
        cake_box[i] = cake[i].getRect()
    
    class Cake:
        def _init_self(self, fname):
            self._image = pygame.image.load(fname)
            self._box = self._image.getRect()
            
    for i in range(6):
        cake[i] = Cake(cake_name[i])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    