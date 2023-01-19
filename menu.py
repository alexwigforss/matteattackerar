import os
import pygame
from pygame.locals import * # QUIT event needs this
# https://www.codecademy.com/article/normalization
# https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
# DID hovercheck
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

# defining fonts
smallfont = pygame.font.SysFont('Corbel',30)
xsmallfont = pygame.font.SysFont('Corbel',15)

# defining colors
white = (255,255,255) # White color
black = (0,0,0) # White color
blue = (0,0,255) # Blue
green = (0,255,0) # Almost Black Green
gray = (150,150,150)

options = [['Starta','Spelläge','Level','Användare','Instruktioner','Avsluta'],
['AddSub','Multi','Divi','Eqvation','Tillbaka'],
['Noobie','Regular','Master','Tillbaka'],
['Lotta','Janne','Fia','Ny Användare','Tillbaka'],
['Talen faller emot dig','','','','','','','','','','Tillbaka']]
# TODO Utred varför outofrange om den sista har ett värde till
menu = 0


# Sparar Fönstrets Dimensioner I Två Variabler
started = False
width = screen.get_width()
height = screen.get_height()
xmargin = width/3-(width/3/3)
ymargin = xmargin/2
y_size = height-ymargin*2

def reHeight():
    global h_unit, y_size, options, fh_unit
    h_unit = y_size/len(options[menu])
    fh_unit = h_unit/4
#reHeight()

def reInit():
    global texts, attrib_texts, attrib_label_dark, attrib_label_light
    texts = []
    attrib_texts = ['','AddSub','Regular','Lotta','','']
    attrib_label_dark = []
    attrib_label_light = []
#reInit()

def reText():
    global smallfont, xsmallfont, white, black, blue, options, menu, texts, attrib_texts, attrib_label_dark, attrib_label_light
    for each in enumerate(options[menu]):
        texts.append(smallfont.render(each[1] , True , blue))
        if menu == 0:
            attrib_label_dark.append(xsmallfont.render(attrib_texts[each[0]] , True , black))
            attrib_label_light.append(xsmallfont.render(attrib_texts[each[0]] , True , white))
#reText()

def threeInRow():
    reHeight()
    reInit()
    reText()
threeInRow()


# for each in enumerate(options[menu]):
#     texts.append(smallfont.render(each[1] , True , blue))
#     attrib_label_dark.append(xsmallfont.render(attrib_texts[each[0]] , True , black))
#     attrib_label_light.append(xsmallfont.render(attrib_texts[each[0]] , True , white))

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
        if ev.type == pygame.MOUSEBUTTONDOWN:        #Checks if a Mouse is clicked
            # Then we check where we clicked
            mouse = pygame.mouse.get_pos()
            ymouse = mouse[1]-ymargin
            choosen = mousyToEntry(ymouse,0,height-ymargin*2,len(options[menu]))
            print(mouse,y_size,'whitin',ymouse,choosen)
            if menu == 0:
                if choosen == 0:
                #import mathAttacks
                    screen = pygame.display.set_mode((res), flags=pygame.HIDDEN)
                    os.system("py mathAttacks.py")
                    print("Back From Game")
                    screen = pygame.display.set_mode((res), flags=pygame.SHOWN)
                elif choosen == 1:
                    menu = 1
                    threeInRow()
                elif choosen == 2:
                    menu = 2
                    threeInRow()
                elif choosen == 3:
                    menu = 3
                    threeInRow()
                elif choosen == 4 and menu == 0:
                    menu = 4
                    threeInRow()
                elif choosen == len(options[menu])-1:
                    print(choosen)
                    pygame.quit()
                    exit()
            elif choosen == len(options[menu])-1:
                print(choosen)
                menu = 0
                threeInRow()

        

    pygame.draw.rect(screen,white,[10,10,width-20,height-20])

    bg(0,0)

    for each in enumerate(options[menu]):
        ts = smallfont.size(options[menu][each[0]])
        hw = ts[0]/2 # halva textens bredd
        if menu == 0:
            atts = xsmallfont.size(attrib_texts[each[0]])
            a_hw = atts[0]/2 # halva textens bredd
        if each[0]==choosen:
            pygame.draw.rect(ss,white,[xmargin,ymargin+each[0]*h_unit+2,width-xmargin*2,h_unit-2])
        else:
            pygame.draw.rect(s,white,[xmargin,ymargin+each[0]*h_unit+2,width-xmargin*2,h_unit-2])
        ss.blit(texts[each[0]],(width/2-hw,ymargin+ts[1]+each[0]*h_unit-(fh_unit)))
        if menu == 0:
            ss.blit(attrib_label_dark[each[0]],(width/2-a_hw,ymargin+ts[1]+each[0]*h_unit+(fh_unit)))
    screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
    screen.blit(ss, (0,0))    # (0,0) are the top-left coordinates
    mouse = pygame.mouse.get_pos()
    if (mouse[0]>xmargin and mouse[0] < width-xmargin) and (mouse[1]>ymargin and mouse[1] < height-ymargin):
        ymouse = mouse[1]-ymargin
        choosen = mousyToEntry(ymouse,0,height-ymargin*2,len(options[menu]))
    #    print(mouse,y_size,'whitin',ymouse,choosen)
        
    # else:
    #     print(mouse,y_size,'outside')
    pygame.display.flip()     # next frame
    #pygame.display.update()     # next frame
    clock.tick(60)
