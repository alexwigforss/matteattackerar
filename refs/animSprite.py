import pygame as pg
import os
clock = pg.time.Clock() 
screen = pg.display.set_mode((400, 400))
pg.time.set_timer(pg.USEREVENT, 250)  # 
sprites = []
for item in range(5):
    sprites.append(pg.image.load("sprites\\"+str(item)+".png"))
    print(item)

dark = (100,50,100) # dark shade of the button
# print(sprite)
width = screen.get_width()
height = screen.get_height()
loop = 1
frame = 0
i = 0
c = 1
while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0
        if event.type == pg.USEREVENT:
            pg.time.set_timer(pg.USEREVENT, 250)  # 
            pg.draw.rect(screen, dark, [0, 0, width, height])
            screen.blit(sprites[i], (100, 100))
            i += c
            frame += 1
            if i == 4:
                c = -1
            elif i == 0:
                c = 1
        
    pg.display.flip()
    clock.tick(60)

pg.quit()