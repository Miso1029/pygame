import sys
import pygame as pygame
from pygame.locals import QUIT
from pygame.locals import *

round = 1
life1 = True
life2 = True
deadthing1 = 0
deadthing2 = 0
End = False
end = 0

def check_rect_collide0(rect_blackbear1, rect_ice):
    if (rect_blackbear1.bottom > rect_ice.top and 
        rect_blackbear1.top < rect_ice.bottom and 
        rect_blackbear1.right > rect_ice.left and 
        rect_blackbear1.left < rect_ice.right):
        return deadthing1+1 and dice()
    return null
    
def check_rect_collide1(rect_blackbear1, rect_donuts):
    if (rect_blackbear1.bottom > rect_donuts.top and 
        rect_blackbear1.top < rect_donuts.bottom and 
        rect_blackbear1.right > rect_donuts.left and 
        rect_blackbear1.left < rect_donuts.right):
        return deadthing1+1 and ddonuts()
    return null

def check_rect_collide2(rect_blackbear1, rect_macaron):
    if (rect_blackbear1.bottom > rect_macaron.top and 
        rect_blackbear1.top < rect_macaron.bottom and 
        rect_blackbear1.right > rect_macaron.left and 
        rect_blackbear1.left < rect_macaron.right):
        return deadthing1+1 and dmacaron()
    return null

def check_rect_collide3(rect_blackbear2, rect_cake):
    if (rect_blackbear2.bottom > rect_cake.top and 
        rect_blackbear2.top < rect_cake.bottom and 
        rect_blackbear2.right > rect_cake.left and 
        rect_blackbear2.left < rect_cake.right):
        return deadthing2+1 and dcake()
    return null  

def dice():
    del ice

def ddonuts():
    del donuts

def dmacaron():
    del macaron

def dcake():
    del cake

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

    
    ice = pygame.image.load("resources/png/ice.png")
    ice.convert()
    rect_ice = ice.get_rect()
    x0 = 50 
    y0 = 50
    
    donuts = pygame.image.load("resources/png/donuts.png")
    donuts.convert()
    rect_donuts = donuts.get_rect()
    x1 = 700
    y1 = 50
    
    macaron = pygame.image.load("resources/png/macaron.png")
    macaron.convert()
    rect_macaron = macaron.get_rect()
    x2 = 700
    y2 = 500
    
    cake = pygame.image.load("resources/png/cake.png")
    cake.convert()
    rect_cake = cake.get_rect()
    x3 = 700
    y3 = 50
    
    blackbear1 = pygame.image.load("resources/png/blackbear1.png")
    blackbear1.convert()
    rect_blackbear1 = blackbear1.get_rect()
    x4 = 50
    y4 = 500
    
    blackbear2 = pygame.image.load("resources/png/blackbear2.png")
    blackbear2.convert()
    rect_blackbear2 = blackbear2.get_rect()
    x5 = 50
    y5 = 500
    
    end1 = pygame.image.load("resources/png/yes.png")
    end1.convert()
    x6 = 100
    y6 = 150
    
    end2 = pygame.image.load("resources/png/no.png")
    end2.convert()
    x7 = 100
    y7 = 150
    
            
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x4 += -50
                    x5 += -50
                if event.key == K_RIGHT:
                    x4 += 50
                    x5 += 50
                if event.key == K_UP:
                    y4 += -50
                    y5 += -50
                if event.key == K_DOWN:
                    y4 += 50
                    y5 += 50
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if round == 1:
                if life1 == True:
                    if x0 < 50 or x0 > 750:
                        x0 = 50
                    if y0 < 50 or y0 > 550:
                        y0 = 50
                    if x1 < 50 or x1 > 750:
                        x1 = 700
                    if y1 < 50 or y1 > 550:
                        y1 = 50
                    if x2 < 50 or x2 > 750:
                        x2 = 700
                    if y2 < 50 or y2 > 550:
                        y2 = 500    

                    x0 += 10
                    y0 += 10
                    x1 += -10
                    y1 += 10
                    x2 += -10
                    y2 += -10                
                    
                    win.fill((255, 255, 255))
                    win.blit(blackbear1, (x4, y4))
                    win.blit(ice, (x0, y0))
                    win.blit(donuts, (x1, y1))
                    win.blit(macaron, (x2, y2))
                    pygame.display.update()
                    pygame.time.wait(500)
                    check_rect_collide0(rect_blackbear1, rect_ice)
                    check_rect_collide1(rect_blackbear1, rect_donuts)
                    check_rect_collide2(rect_blackbear1, rect_macaron) 
                    
                    if deadthing1 == 3:
                        win.fill((255, 255, 255))
                        pygame.display.update()
                        life1 == False
                        round == 2 
                  
            elif round == 2:
                if life2 == True:
                    win.fill((255, 255, 255))   
                    round_surface = head_font.render('Round2', True, (0, 0, 0))  
                    win.blit(round_surface, (300, 100))   
                    pygame.display.update()  
                    pygame.time.wait(1000)
                    
                    if x3 < 50 or x3 > 750:
                        x3 = 700
                    if y3 < 50 or y3 > 550:
                        y3 = 50                    
                    
                    win.fill((255, 255, 255))
                    win.blit(blackbear2, (x5, y5))
                    win.blit(cake, (x3, y3))
                    pygame.display.update()
                    pygame.time.wait(500)
                    check_rect_collide3(rect_blackbear2, rect_cake)
                    
                    if deadthing2 == 1:
                        win.fill((255, 255, 255))
                        pygame.display.update()
                        life2 == False
                        End == True
                        end == 1   
                    else:
                        win.fill((255, 255, 255))
                        pygame.display.update()
                        End == True
                        end == 2
            else:
                null
            
            if End == True:
                if end == 1:
                    win.fill((255, 255, 255))
                    win.blit(end1, (x6, y6))
                    pygame.display.update()
                    pygame.time.wait(5000)
                else:
                    win.fill((255, 255, 255))
                    win.blit(end2, (x7, y7))
                    pygame.display.update()
                    pygame.time.wait(5000)
    
    
if __name__ == "__main__":
    main()    
 
