import pygame
import time

import random
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

height=480
width=640

box=10
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Snake')

lead_x=width/2
lead_y=height/2

lead_x_change=0
lead_y_change=0

randx=round(random.randrange(0,width-box)/10.0)*10.0
randy=round(random.randrange(0,height-box)/10.0)*10.0

snakeList=[]
snakeLength=1
clock=pygame.time.Clock()
score=0
font=pygame.font.SysFont(None,25)
font1=pygame.font.SysFont(None,25)
def text_msg(msg,color):
    text=font.render(msg,True,color)
    screen.blit(text,[width/2-200,height/2])

def text_score(score,color):
    text=font1.render('Score: '+str(score),True,color)
    screen.blit(text,[25,25])
    
def text_length(l,color):
    length=font1.render('Length of a snake: '+str(l),True,color)
    screen.blit(length,[125,25])

def snake(box,snakelist):
    for xny in snakelist:
        pygame.draw.rect(screen,green,[xny[0],xny[1],box,box])

start=time.time()
check=0
print (start)

while True:
    
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                lead_x_change=-10
                lead_y_change=0
            if event.key==pygame.K_RIGHT:
                lead_x_change=10
                lead_y_change=0
            if event.key==pygame.K_UP:
                lead_y_change=-10
                lead_x_change=0
            if event.key==pygame.K_DOWN:
                lead_y_change=10
                lead_x_change=0
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                lead_x_change=0

        
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                lead_y_change=0
        
    lead_x += lead_x_change
    lead_y += lead_y_change
    #print (lead_x)

    if snakeLength<=0:
        text_msg('You lose, loss all segement of the snake.',red)
        pygame.display.update()
        time.sleep(2)
        screen.fill(white)
        text_msg('Game over!',blue)
        pygame.display.update()
        time.sleep(5)    
        pygame.quit()
        quit()
    if lead_y>height-box or lead_x<0 or lead_y<0 or lead_x>width-box:
        text_msg('You lose, go outside you fool',red)
        pygame.display.update()
        time.sleep(2)
        screen.fill(white)
        text_msg('Game over!',blue)
        pygame.display.update()
        time.sleep(5)    
        pygame.quit()
        quit()
    
    screen.fill(white)
    pygame.draw.rect(screen,red,[randx,randy,box,box])
    #pygame.draw.rect(screen,green,[lead_x,lead_y,box,box])
    
    snakeHead=[]
    snakeHead.append(lead_x)
    snakeHead.append(lead_y)
    snakeList.append(snakeHead)
    if len(snakeList)>snakeLength:
        del snakeList[0]
    #print (snakeList,snakeHead)
    
    stop=time.time()
    print(stop-start)
    if (stop-start)>10:
        start=time.time()
        if score>0:
            snakeList.pop()
        snakeLength-=1
    if snakeLength==10:
        text_msg('You win !',red)
        pygame.display.update()
        time.sleep(2)
        screen.fill(white)
        text_msg('Game over!',blue)
        pygame.display.update()
        time.sleep(5)    
        pygame.quit()
        quit()
    print(snakeLength,snakeList)
        
        
        
        
    snake(box,snakeList)
    text_score(score,blue)
    text_length(snakeLength,red)
    if lead_x==randx and lead_y==randy:
        print ('collision')
        randx=round(random.randrange(0,width-box)/10.0)*10.0
        randy=round(random.randrange(0,height-box)/10.0)*10.0
        snakeLength+=1
        score+=1
        
    
    pygame.display.update()
    clock.tick(15)
    



