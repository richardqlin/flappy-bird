import pygame,sys
from pygame.locals import *

import pdb

screen=pygame.display.set_mode((640,480))
center_x=320
center_y=240
left_pad_y=240
right_pad_y=240
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
left_down=0
left_up=0
right_down=0
right_up=0
left_hit=0
right_hit=0
firsthit=0
speed_y=0
z=0
a=0
pygame.init()
font=pygame.font.SysFont('times.ttf',32)
score=0
scorel=z
scorer=a
pygame.display.set_caption('Pong Pong!')


while True:
    screen.fill((0,0,0)) #Black
    pygame.draw.line(screen,white,(320,0),(320,480),5)
    scorel_display=font.render(str(scorel),False,white)
    scorer_display=font.render(str(scorer),False,white)
    screen.blit(scorel_display,(250,210))
    screen.blit(scorer_display,(380,210))
    pygame.draw.circle(screen,blue,(center_x,center_y),7,7)
    pygame.draw.rect(screen,green,(10,left_pad_y,10,50))
    pygame.draw.rect(screen,red,(620,right_pad_y,10,50))
    
    for event in pygame.event.get():
        
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_RIGHT:
                left_down=1
            elif event.key==K_LEFT:
                left_up=1
            if event.key==K_DOWN:
                right_down=1
            elif event.key==K_UP:
                right_up=1
        
        elif event.type==KEYUP:
            if event.key==K_RIGHT:
                left_down=0
            elif event.key==K_LEFT:
                left_up=0
            if event.key==K_DOWN:
                right_down=0
            elif event.key==K_UP:
                right_up=0
        
####################################
        #Ball Placement
####################################
    if center_x<=640 and center_x>=0:
        if firsthit==0:
            center_x+=1
            
            
        if center_x==638:
            center_x=320
            center_y=240
            speed_y=0
            
            print('rlost')
            scorel+=1
            #firsthit=0
            
        elif center_x==2:
            center_x=320
            center_y=240
            speed_y=0
            scorer+=1
            
            print('llost')
            #firsthit=1
#####################################            
        #Paddle Movement
#####################################
    if left_down==1 and left_pad_y!=430:
        left_pad_y+=2.5
        if left_pad_y==430:
            left_down=0
    elif left_up==1 and left_pad_y!=0:
        left_pad_y-=2.5
        if left_pad_y==0:
            left_up=0
    if right_down==1 and right_pad_y!=430:
        right_pad_y+=2.5
        if right_pad_y==430:
            right_down=0
    elif right_up==1 and right_pad_y!=0:
        right_pad_y-=2.5
        if right_pad_y==0:
            right_up=0
#####################################
        #Ball Rebound
#####################################
    if center_x==620 and right_pad_y-2<center_y<right_pad_y+52:
        right_hit=1
        left_hit=0
        firsthit=1
        print ('collision')
        print (center_x,right_pad_y-2,center_y,right_pad_y+52)
        print(speed_y)
        #speed_y=1
        if center_x==620 and right_pad_y-2<center_y<right_pad_y+15:
            speed_y=1
    elif center_x==20 and left_pad_y-2<center_y<left_pad_y+52:
        left_hit=1
        right_hit=0
        firsthit=1
        #speed_y=1
        if center_x==20 and left_pad_y-2<center_y<left_pad_y+15:
            speed_y=1
#####################################
        
#####################################
    if right_hit==1:
        center_x-=1
        center_y+=speed_y
        #print('right_hit',center_y)
    if left_hit==1:
        center_x+=1
        center_y+=speed_y
        #print('left_hit',center_y)
    if center_y==480:
        speed_y=-speed_y
    if center_y==0:
        speed_y=-speed_y
#####################################


#########
    pygame.display.update()
    pygame.time.delay(5)
    
