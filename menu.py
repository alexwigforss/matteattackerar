import pygame
from pygame.locals import * # QUIT event needs this
# https://www.codecademy.com/article/normalization
# TODO hovercheck
# TODO kanske lite marginal runt knapparna
# TODO meny för att välja gamemode, level, instruktioner & highscore
# TODO lets se if this is caught
"""
Get package failed, please run
"pip list --format json" or "pip3 list --format json"
check pip support json format
"""
pygame.init() # initializing the constructor
clock = pygame.time.Clock()
res = (720,640) # Fönstrets storlek
screen = pygame.display.set_mode((res), pygame.DOUBLEBUF, 32)
bgImg = pygame.image.load('assets\BGTEST.JPG')
bgImg = pygame.transform.smoothscale(bgImg, (1440, 1280))
s = pygame.Surface(res, pygame.SRCALPHA, 32)
s = s.convert_alpha()
s.set_alpha(180)                # alpha level
ss = pygame.Surface(res, pygame.SRCALPHA, 32)
ss = s.convert_alpha()
ss.set_alpha(225)               # alpha level
choosen = 1
def bg(x,y):
    screen.blit(bgImg, (x-360,y-320))

white = (255,255,255) # White color
black = (0,0,0) # White color
blue = (0,0,255) # Blue
green = (0,255,0) # Almost Black Green
gray = (150,150,150)

options = [['Starta','Spelläge','Level','Användare','Instruktioner','Avsluta'],
['AddSub','Multi','Divi','Eqvation','Avsluta'],['Tester Testson','Ny Användare'],
['Noobie','Regular','Master'],
['Tester Testson','Ny Användare']]
menu = 0

# Sparar Fönstrets Dimensioner I Två Variabler
width = screen.get_width()
height = screen.get_height()
xmargin = width/3-(width/3/3)
ymargin = xmargin/2
y_size = height-ymargin*2
h_unit = y_size/len(options[menu])
fh_unit = h_unit/4
started = False
# defining a font
smallfont = pygame.font.SysFont('Corbel',30)
xsmallfont = pygame.font.SysFont('Corbel',15)
# rendering some texts written in this font
text = smallfont.render('start' , True , blue)


texts = []
attrib_texts = ['','andra','tredje','fjärde','femte','']
attrib_label_dark = []
attrib_label_light = []

for each in enumerate(options[menu]):
    texts.append(smallfont.render(each[1] , True , blue))
    attrib_label_dark.append(xsmallfont.render(attrib_texts[each[0]] , True , black))
    attrib_label_light.append(xsmallfont.render(attrib_texts[each[0]] , True , white))

def mousyToEntry(value,min,max,entries):
    percentage = (value - min) / (max - min)
    return int(percentage * entries)

while started == False:
    # clear display
    screen.fill((white))
    s.fill((0,0,0,0))
    ss.fill((0,0,0,0))
    s = s.convert_alpha()
    ss = ss.convert_alpha()
    for ev in pygame.event.get():
        # Check for Sys Events
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen,white,[10,10,width-20,height-20])

    bg(0,0)

    for each in enumerate(options[menu]):
        ts = smallfont.size(options[menu][each[0]])
        hw = ts[0]/2 # halva textens bredd
        atts = xsmallfont.size(attrib_texts[each[0]])
        a_hw = atts[0]/2 # halva textens bredd
        if each[0]==choosen:
            pygame.draw.rect(ss,white,[xmargin,ymargin+each[0]*h_unit+2,width-xmargin*2,h_unit-2])
        else:
            pygame.draw.rect(s,white,[xmargin,ymargin+each[0]*h_unit+2,width-xmargin*2,h_unit-2])
            
        ss.blit(attrib_label_dark[each[0]],(width/2-a_hw,ymargin+ts[1]+each[0]*h_unit+(fh_unit)))
        ss.blit(texts[each[0]],(width/2-hw,ymargin+ts[1]+each[0]*h_unit-(fh_unit)))
    screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
    screen.blit(ss, (0,0))    # (0,0) are the top-left coordinates
    mouse = pygame.mouse.get_pos()
    if (mouse[0]>xmargin and mouse[0] < width-xmargin) and (mouse[1]>ymargin and mouse[1] < height-ymargin):
        ymouse = mouse[1]-ymargin
        choosen = mousyToEntry(ymouse,0,height-ymargin*2,6)
        print(mouse,y_size,'whitin',ymouse,choosen)
    else:
        print(mouse,y_size,'outside')
    pygame.display.flip()     # next frame
    #pygame.display.update()     # next frame
    clock.tick(60)
