import sys
import pygame
from pygame.locals import QUIT
from pygame.locals import *

class Dessert:
    def _init_self(self, fname):
        self._image = pygame.image.load(fname)
        self._box = self._image.getRect()

def check_rect_collide0(rect_blackbear1, dessert_box[0])bool:
    if rect_blackbear1.bottom > dessert_box[0].top and 
       rect_blackbear1.top < dessert_box[0].bottom and 
       rect_blackbear1.right > dessert_box[0].left and 
       rect_blackbear1.left < dessert_box[0].right:
        return deadthing1 += 1
    return null

def check_rect_collide1(rect_blackbear1, dessert_box[1]):
    if rect_blackbear1.bottom > dessert_box[1].top and 
       rect_blackbear1.top < dessert_box[1].bottom and 
       rect_blackbear1.right > dessert_box[1].left and 
       rect_blackbear1.left < dessert_box[1].right:
        return deadthing1 += 1
    return null

def check_rect_collide2(rect_blackbear1, dessert_box[2]):
    if rect_blackbear1.bottom > dessert_box[2].top and 
       rect_blackbear1.top < dessert_box[2].bottom and 
       rect_blackbear1.right > dessert_box[2].left and 
       rect_blackbear1.left < dessert_box[2].right:
        return deadthing1 += 1
    return null

def check_rect_collide3(rect_blackbear2, dessert_box[3]):
    if rect_blackbear2.bottom > dessert_box[3].top and 
       rect_blackbear2.top < dessert_box[3].bottom and 
       rect_blackbear2.right > dessert_box[3].left and 
       rect_blackbear2.left < dessert_box[3].right:
        return deadthing2 += 1
    return null

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
    life1 = True
    life2 = True
    deadthing1 = 0
    deadthing2 = 0
    End = False
    end = 0
  
    blackbear1 = pygame.image.load("resources/png/blackbear1.png")
    blackbear1.convert()
    rect_blackbear1 = blackbear1.getRect()
    x4 = 50
    y4 = 500
    
    blackbear2 = pygame.image.load("resources/png/blackbear2.png")
    blackbear2.convert()
    rect_blackbear2 = blackbear2.getRect()
    x5 = 50
    y5 = 500
    
    dessert = []
    dessert_box = []
    dessert_name = ["resources/png/ice.png", "resources/png/donuts.png", "resources/png/macaron.png", "resources/png/cake.png"]
    dessert_xy = [(50,50),(700,50),(700,500),(700,50)]
    
    for i in range(4):
        dessert[i] = pygame.image.load(dessert_name)
        dessert_box[i] = dessert[i].getRect()
            
    for i in range(4):
        dessert[i] = Dessert(dessert_name[i])
        dessert_xy[i] = dessert[i]
    
    end1 = pygame.image.load("resources/png/yes.png")
    end1.convert()
    x6 = 100
    y6 = 150
    
    end2 = pygame.image.load("resources/png/no.png")
    end2.convert()
    x7 = 100
    y7 = 150
    
    if round == 2:
        if life2 = True:
            win.fill((255, 255, 255))   
            round_surface = head_font.render('Round2', True, (0, 0, 0))  
            win.blit(round_surface, (300, 100))   
            pygame.display.update()  
            pygame.time.wait(1000)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
            
            while event.type == KEYDOWN:
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

                    y4 = 500
                    x0 += 10
                    y0 += 10
                    x1 += -10
                    y1 += 10
                    x2 += -10
                    y2 += -10                
                    for i in range(3):
                        win.fill((255, 255, 255))
                        win.blit(blackbear1, (x4, y4))
                        win.blit(dessert[i], dessert_xy[i])
                        pygame.display.update()
                        pygame.time.wait(500)
                    check_rect_collide0(rect_blackbear1, dessert_box[0])
                    check_rect_collide1(rect_blackbear1, dessert_box[1])
                    check_rect_collide2(rect_blackbear1, dessert_box[2])                    
                    if deadthing1 == 3:
                        life1 == False
                        round == 2 
                  
            elif round == 2:
                if life2 = True:
                    if x3 < 50 or x3 > 750:
                        x3 = 700
                    if y3 < 50 or y3 > 550:
                        y3 = 50                    
                    win.fill((255, 255, 255))
                    win.blit(blackbear2, (x5, y5))
                    win.blit(dessert[3], dessert_xy[3])
                    pygame.display.update()
                    pygame.time.wait(500)
                    check_rect_collide3(rect_blackbear2, dessert_box[3])
                    if deadthing2 == 1:
                        life2 == False
                        End == True
                        end == 1   
                    else:
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
 
