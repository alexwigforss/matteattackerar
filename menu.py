import pygame
from pygame.locals import * # QUIT event needs this

# TODO hovercheck
# TODO kanske lite marginal runt knapparna
# TODO inför poängsystem. dubbla poängen om man tar en sten i luften
# TODO meny för att välja gamemode, level, instruktioner & highscore
# TODO lets se if this is caught

pygame.init() # initializing the constructor
# res = (520,540) # Fönstrets storlek
res = (720,640) # Fönstrets storlek
screen = pygame.display.set_mode(res) # Öppnar Ett Fönster

white = (255,255,255) # White color
other = (0,0,255) # Blue
gray = (150,150,150)

# Sparar Fönstrets Dimensioner I Två Variabler
width = screen.get_width()
height = screen.get_height()

started = False
options = [['Tester Testson','Ny Användare'],['Starta','Alternativ','Level','Instruktioner','Avsluta']]

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
# rendering some texts written in this font
text = smallfont.render('start' , True , other)

texts = []

for each in options[0]:
    texts.append(smallfont.render(each , True , other))

while started == False:
    for ev in pygame.event.get():
        # Check for Sys Events
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen,white,[10,10,width-20,height-20])

    for each in enumerate(options[0]):
        ts = smallfont.size(options[0][each[0]])
        hw = ts[0]/2 # halva textens bredd
        hh = ts[1]/2 # halva textens höjd
        pygame.draw.rect(screen,gray,[100,100+each[0]*100,width-200,100])
        screen.blit(texts[each[0]],(width/2-hw,100+ts[1]+each[0]*100))

    pygame.display.update()     # next frame

