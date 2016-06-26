import pygame
import random

from os import path

img_dir=path.join(path.dirname(__file__),'img')

width=600
height=600


white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,255,0)


#initialize pygame and create window

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("my game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player_img,(40,40))
        self.image.set_colorkey(black)
        #self.image.fill(green)
        self.rect=self.image.get_rect()
        self.rect.centerx=width/2
        self.rect.bottom=height-10
        self.speedx=0

    def update(self):
        self.speedx=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-5
        if keystate[pygame.K_RIGHT]:
            self.speedx=5
        self.rect.x+=self.speedx
        if self.rect.right>width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
        #print(self.speedx,self.rect.x)

    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(monstor_img,(40,30))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(width-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,4)

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.top>height+10:
            self.rect.x=random.randrange(width-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(1,4)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_img
        self.image.set_colorkey(black)
        
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-5

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()
            

#load all game images

player_img=pygame.image.load(path.join(img_dir,'ship-medium.png')).convert()
bullet_img=pygame.image.load(path.join(img_dir,'laserRed16.png')).convert()
monstor_img=pygame.image.load(path.join(img_dir,'monstor.png')).convert()

all_sprites=pygame.sprite.Group()

mobs=pygame.sprite.Group()

bullets=pygame.sprite.Group()

player=Player()
all_sprites.add(player)

for i in range(10):
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)
    
done=True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        m=Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits=pygame.sprite.spritecollide(player,mobs,False)
    if hits:
        print('lost game')
        done=False
    
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(10)
    
