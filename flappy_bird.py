import pygame
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

height=600
width=800
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Flappy Bird')

def ball(x,y):
    pygame.draw.circle(screen,black,(x,y),20)

def gameover():
    font=pygame.font.SysFont(None,75)
    text=font.render('Game Over', True,red)
    screen.blit(text,( int(width/2)-40,int(height/2)))

def obstacle(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen,green,(xloc,yloc,xsize,ysize))
    pygame.draw.rect(screen,green,(xloc,int(yloc+ysize+space), xsize,ysize+height-space))

def Score(score):
    font=pygame.font.SysFont(None,50)
    text =font.render('Score: '+str(score), True, blue)
    screen.blit(text,(10,10))


x=int(width/2)
y=int(height/2)

x_change=0
y_change=0

ground=height
xloc=width
yloc=0
xsize=70
ysize=random.randint(0,int(width/2))
space=150
obchange=3
score=0

done=True

clock=pygame.time.Clock()

FPS=40
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                y_change=-10
        if event.type==pygame.KEYUP:
            
            if event.key==pygame.K_UP:
                y_change=5

    screen.fill(white)
    obstacle(xloc, yloc, xsize, ysize)
    ball(x,y)
    print(x,y)
    Score(score)
    
    y+=y_change
    xloc-=obchange

    if y>height-10 or y<10:
        gameover()
        y_change=0
        obchange=0
    
    if xloc < x+20 and x-15 <xsize+xloc and y-20 < ysize :
        gameover()
        obchange=0
        y_change=0
        
    if xloc < x+20 and y+20 >ysize+space and x-15 <xsize+xloc:
        gameover()
        obchange=0
        y_change=0    
    
    if xloc<-80:
        xloc=width
        ysize=random.randint(0,int(height/2))

    if xloc < x <xloc+3:
        score=score+1
    #print(xloc,ysize)
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
