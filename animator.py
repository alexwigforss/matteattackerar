# [x] BUG Rescaling all sprites on 
# [ ] TODO test multiple instances
# [ ] TODO get dimensions by monsters or main

import pygame
import os
import pygame as pg
import monsters as m

class Animation:
    framecount = 0
    dir = 1
    def __init__(self,width,height):
        self.sprites = []
        self.dir = 1
        self.framecount = 0
        self.width = width
        self.height = height

        for item in range(5):
            if os.name == 'posix':
                self.sprites.append(pg.image.load("sprites/" + str(item) + ".png"))
            elif os.name == 'nt':
                self.sprites.append(pg.image.load("sprites\\" + str(item) + ".png"))

        for item in range(5):
            self.sprites[item] = pygame.transform.scale(self.sprites[item], (self.width, self.height))

    def blitNextFrame(self,screen,x,y):
        screen.blit(self.sprites[self.framecount], (x, y))
        self.framecount += self.dir

        if self.framecount == 4:
            self.dir = -1
        elif self.framecount == 0:
            self.dir = 1

    def blitStatic(self,screen,x,y):
        screen.blit(self.sprites[2], (x, y))

if __name__ == "__main__":
    clock = pg.time.Clock()
    screen = pg.display.set_mode((400, 400))
    pg.time.set_timer(pg.USEREVENT, 250)
    
    anims = []
    anims.append(Animation(100,50))
    # anim = Animation(100,50)
    black = (255, 255, 255)
    dark = (100, 50, 100)
    
    width = screen.get_width()
    height = screen.get_height()
    
    loop = 1
    sprite_y = 0
    speed = 1
    
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = 0
            if event.type == pg.USEREVENT:
                pg.time.set_timer(pg.USEREVENT, 250)
                pg.draw.rect(screen, dark, [0, 0, width, height])

                sprite_y += speed
                if sprite_y == 10:
                    anims.append(Animation(100,50))

                if sprite_y > height:
                    sprite_y = 0

                i = 0
                for item in anims:
                    item.blitNextFrame(screen,i, sprite_y)
                    i += 100
        
        pg.display.flip()
        clock.tick(120)