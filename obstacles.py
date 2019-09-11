import pygame as pg
from settings import *
import os
import random

vec = pg.math.Vector2
screen = pg.display.set_mode((640, 480))

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")


'''class Obstacles(pg.sprite.Sprite):
   def __init__(self):
         pg.sprite.Sprite.__init__(self)
         self.image = pg.image.load("img/Chicken_Walk/spr_sportscar_0.png").convert_alpha()
         self.image.set_colorkey((0,0,0))
         self.rect = self.image.get_rect()
         self.rect.centerx = WIDTH /2
         self.rect.bottom = HEIGHT  -2
         self.speedx = 0'''

class Mob(pg.sprite.Sprite):
   def __init__(self):
       pg.sprite.Sprite.__init__(self)
       self.image = pg.Surface((15, 20))
       self.image = pg.image.load("img/hotdog.png").convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.x = random.randrange(HEIGHT - self.rect.height)
       self.rect.x = random.randrange(-20, -10)
       self.speedy = random.randrange(0, 5)
       self.speedx = random.randrange(-2, 10)

   

   def update(self):
      self.rect.x += self.speedx
      self.rect.x += self.speedy
      #the code below directs the sprites to move from left to right
      if self.rect.centery > WIDTH + 9  or self.rect.right < -26 or self.rect.left > HEIGHT + 19:
         self.rect.y = random.randrange(WIDTH - self.rect.width)
         self.rect.x = random.randrange(-100, -40)
         self.speedx = random.randrange(-1, 5)






         
'''def update(self, dt):
      self.rect.x += self.vx * dt
      if self.rect.left > WIDTH :
      self.rect.right = 0  '''  

