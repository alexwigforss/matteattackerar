import os
import pygame as pg

clock = pg.time.Clock()
screen = pg.display.set_mode((400, 400))
pg.time.set_timer(pg.USEREVENT, 250)

sprites = []
for item in range(5):
    if os.name == 'posix':
        sprites.append(pg.image.load("sprites/" + str(item) + ".png"))
    elif os.name == 'nt':
        sprites.append(pg.image.load("sprites\\" + str(item) + ".png"))

black = (255, 255, 255)
dark = (100, 50, 100)

width = screen.get_width()
height = screen.get_height()

loop = 1
frame = 0
i = 0
c = 1

sprite_x = 0
sprite_y = 0
speed = 1
sprite_height = sprites[0].get_height()

while loop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = 0
        if event.type == pg.USEREVENT:
            pg.time.set_timer(pg.USEREVENT, 250)
            pg.draw.rect(screen, dark, [0, 0, width, height])

            sprite_y += speed

            if sprite_y > height - sprite_height:
                sprite_y = 0

            screen.blit(sprites[i], (sprite_x, sprite_y))
            i += c
            frame += 1

            if i == 4:
                c = -1
            elif i == 0:
                c = 1

    pg.display.flip()
    clock.tick(120)

pg.quit()
