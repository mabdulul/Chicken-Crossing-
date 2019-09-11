# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 1
# Video link: https://www.youtube.com/watch?v=uWvb3QzA48c
# Project setup

import pygame as pg
import random
from settings import *
from sprites import *
from obstacles import *
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        #pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(font_name)

    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        p1 = Platform(0, HEIGHT - 40, WIDTH, 50)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform( 0 , WIDTH / 2, WIDTH, 50)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        p3 = Platform( 0 ,50, WIDTH, 50)
        self.all_sprites.add(p3)
        self.platforms.add(p3)
        self.player = Player()
        self.all_sprites.add(self.player)
        
        


        # Adding the obstacles
        self.mobs = pg.sprite.Group()
        for i in range(20):
            m = Mob()
            self.all_sprites.add(m)
            self.mobs.add(m)
        self.run()
        


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.hits = pg.sprite.spritecollide(self.player, self.mobs, False)
        if self.hits:
            self.show_go_screen()
        keys = pg.key.get_pressed()  
        if  keys[pg.K_UP]:
               self.score += 1
        elif keys[pg.K_DOWN]:
               self.score = self.score
       
    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.background_image_two = pg.image.load(os.path.join(img_folder,"road.jpg"))
        self.screen.blit(self.background_image_two, [0,0])
        self.image = pg.image.load(os.path.join(img_folder,"Back_TwoFoot2.png")).convert_alpha()
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(WHITE)
        self.background_image = pg.image.load(os.path.join(img_folder,"start_screen.png"))
        self.screen.blit(self.background_image, [0,0])
        self.draw_text("Arrows to move and Press a key to play",12, BLACK, WIDTH/2, HEIGHT * 3 / 4 )
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
        # Start walking from the bottom/center
        
    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for events in pg.event.get():
                if events.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if events.type == pg.KEYUP:
                    waiting = False
    
    def draw_text(self,text,size, color, x, y):
        font = pg.font.Font(self.font_name, 30)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()