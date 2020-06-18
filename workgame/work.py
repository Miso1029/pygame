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
  
  win.fill((255, 255, 255))
  blackbear1 = pygame.image.load("resources/png/blackbear1.png")
  blackbear1.convert()
  x1 = 50
  y1 = 500
  win.blit(blackbear1, (x1, y1))

  
  ice = pygame.image.load("resources/png/ice.png")  
  ice.convert() 
  x2 = 50
  y2 = 50
  win.blit(ice, (x2, y2))
  
  donuts = pygame.image.load("resources/png/donuts.png") 
  donuts.convert()
  x3 = 700
  y3 = 50
  win.blit(donuts, (x3, y3))
  
  macaron = pygame.image.load("resources/png/macaron.png")  
  macaron.convert()
  x4 = 700
  y4 = 500  
  win.blit(macaron, (x4, y4))
  
  pygame.display.update()
  pygame.time.wait(500)
  
  cake = pygame.image.load("resources/png/cake.png") 
  cake.convert()
  x5 = 700
  y5 = 50
  
  blackbear2 = pygame.image.load("resources/png/blackbear2.png")
  blackbear2.convert()
  x6 = 50
  y6 = 500
  
  while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x1 += -50
                x6 += -50
            if event.key == K_RIGHT:
                x1 += 50
                x6 += 50
            if event.key == K_UP:
                y1 += -50
                y6 += -50
            if event.key == K_DOWN:
                y1 += 50
                y6 += 50
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()    
      
        if round == 1:
            if life == True:
                if x2 < 50 or x2 > 750:
                    x2 = 50
                if y2 < 50 or y2 > 550:
                    y2 = 50
                if x3 < 50 or x3 > 750:
                    x3 = 700
                if y3 < 50 or y3 > 550:
                    y3 = 50
                if x4 < 50 or x4 > 750:
                    x4 = 700
                if y4 < 50 or y4 > 550:
                    y4 = 500
                if deadthing == 3:
                    life == False
                 
                x2 += 10
                y2 += 10
                x3 += -10
                y3 += 10
                x4 += -10
                y4 += -10 
                win.fill((255, 255, 255))
                win.blit(blackbear1, (x1, y1))
                win.blit(ice, (x2, y2))
                win.blit(donuts, (x3, y3))
                win.blit(macaron, (x4, y4))
                pygame.display.update()
                pygame.time.wait(500)
                
            
            else:
                round += 2
    
        elif round == 2:
            win.fill((255, 255, 255))   
            round_surface = head_font.render('Round2', True, (0, 0, 0))  
            win.blit(round_surface, (300, 250))   
            pygame.display.update()  
            pygame.time.wait(2000)  
  

if __name__ == "__main__":
    main()