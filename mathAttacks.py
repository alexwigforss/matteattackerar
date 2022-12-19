# DID ge rätt sorlek till rätt tal
# DID få dem att släppas i x-led där det finns plats
# TODO Få dem att falla till botten om det finns plats
# TODO cirkeldiagram ist fär att skriva ut fraktionerna med siffror
# TODO Test test test

legend ="""
 Instruktioner
 --------------------------------------------------------------------------
 Välj Siffror med musen
 När man har en match kan man spränga med space"""
 
import pygame
from pygame.locals import * # QUIT event needs this
import slumpfabrik
import random
import helpers
import monsters
import game

p1 = monsters.Monster(36,200,100)
p1.myfunc()
print(p1)

# init window
clock = pygame.time.Clock()
pygame.init()# initializing the constructor
# res = (520,540) # Fönstrets storlek
res = (720,640) # Fönstrets storlek
screen = pygame.display.set_mode(res)# Öppnar Ett Fönster

pygame.time.set_timer(pygame.USEREVENT, game.DropRate)  # 

# Färger  
white = (255,255,255) # white white
light = (170,170,170) # light shade of the button
dark = (100,100,100) # dark shade of the button
alpha_light = (170,170,170,80) # dark shade of the button

GRAY = (155,155,155)
RED = (170,0,0)
MIXED = (150,0,150)

width = screen.get_width()
height = screen.get_height()

canvas_x = int(150)
canvas_y = int(60)
canvas_w = int(width - canvas_x *2)
canvas_h = int(height - canvas_y *2)

# w_unit = canvas_w / 10
w_unit = canvas_w / 16
monstersizes = [3,4,6,7,10]
#monstersizes = [6,7,9,10,14]

num = lnum = rnum = 0   # Variabler för utdata av användarens val
btn_h = int(height / 10) # Knappars höjd
btn_w = int(140) # Knappars höjd
gap = int(5)

enemy_x = btn_w

tgleft = tgright = -1
gameOver = False
lp = rp = False # Leftpressed and RightPressed
smallfont = pygame.font.SysFont('Corbel',35)
debug_text = smallfont.render('quit' , True , white)
centerQuit = debug_text.get_rect(center=(width/2,35))
txt1 = smallfont.render('1' , True , white)
resnum = smallfont.render(str(num), True, white) 
leftnum = smallfont.render(str(lnum), True, white) 
rightnum = smallfont.render(str(rnum), True, white) 
movetext = smallfont.render('0' , True , (0,0,0))
events = pygame.event.get()

# Where is the mouse cursor
def lefty():
    mus = mouse[1]
    global mouseoverLeft
    mouseoverLeft = getValue()

def righty():
    mus = mouse[1]
    global mouseoverRight
    mouseoverRight = getValue()

def between():
    global mouseoverLeft
    global mouseoverRight
    mouseoverLeft = 0
    mouseoverRight = 0

def getValue():
    return int(mouse[1]/height*10+1)

monster_list = []
list_of_rows_size = []
num_list = []

# Beroende på talets storlek tilldela Typ
def getSizeInd(nr):
    if nr < 11:
        si=0
    elif nr < 31:
        si=1
    elif nr < 51:
        si=2
    elif nr < 71:
        si=3
    else:
        si=4
    return si

rowFilled = 0

def DropBlock():
    global rowFilled
    numberis = slumpfabrik.getRand()
    sizeind = getSizeInd(numberis)
    monster_w = int(w_unit * monstersizes[sizeind])

    if rowFilled + monster_w > canvas_w:
        rowFilled = 0
        xpos = canvas_x
    else:
        xpos = canvas_x + rowFilled

    rowFilled = rowFilled + monster_w

    for r in range(0,1):
        rect = pygame.Rect(xpos, -100, monster_w, 60)
        monster_list.append(rect)
        num_list.append(numberis)
        if len(monster_list) > 10:
            global gameOver
            gameOver = True
DropBlock()

global target
target = -1

def lb_Changed():
    global leftnum,resnum
    leftnum = smallfont.render(str(lnum), True, white)
    resnum = smallfont.render(str(lnum * rnum), True, white) 

def rb_Changed():
    global rightnum,resnum
    rightnum = smallfont.render(str(rnum), True, white)
    resnum = smallfont.render(str(lnum * rnum), True, white) 

#    _  _  _  _____  _  ____     _         ___    ___   ____  
#   | ||_|| |(____ || ||  _ \   | |       / _ \  / _ \ |  _ \ 
#   | |   | |/ ___ || || | | |  | |_____ | |_| || |_| || |_| |
#   |_|   |_|\_____||_||_| |_|  |_______) \___/  \___/ |  __/ 
#                                                      |_|    
once = True

while gameOver == False:
    #   ╦ ╦┌─┐┌─┐┬  ┬┌─┐┬─┐  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐
    #   ╠═╣│ ││ │└┐┌┘├┤ ├┬┘  ║  ├─┤├┤ │  ├┴┐└─┐
    #   ╩ ╩└─┘└─┘ └┘ └─┘┴└─  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # Quit Button
    if 140 <= mouse[0] <= width-140 and 60 >= mouse[1]:
        pygame.draw.rect(screen,light,[0+150,0,width-300,60])
    # Launch Button
    elif 140 <= mouse[0] <= width-140 and height-60 <= mouse[1]:
        pygame.draw.rect(screen,light,[150,height-60,width-300,height])
    # Left panel
    elif 0 <= mouse[0] <= 0+140:
        pygame.draw.rect(screen,alpha_light,[0,0,140,height])
        once = True
        lefty()
    # Right panel
    elif width-140 <= mouse[0] <= width:
        pygame.draw.rect(screen,alpha_light,[width-140,0,width,height])
        once = True
        righty()
    else:
        # Rest of the area ie the canvas
        if once:
            pygame.draw.rect(screen,dark,[0,0,140,height])
            pygame.draw.rect(screen,dark,[width-140,0,width,height])
            once = False
        pass

    #   ╔═╗╦  ╦╔═╗╔╗╔╔╦╗╔═╗
    #   ║╣ ╚╗╔╝║╣ ║║║ ║ ╚═╗
    #   ╚═╝ ╚╝ ╚═╝╝╚╝ ╩ ╚═╝

    for ev in pygame.event.get():
        # Check for Sys Events
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Timer drops new block
        if ev.type == pygame.USEREVENT:
            pygame.time.set_timer(pygame.USEREVENT, game.DropRate)  # 
            game.nrOfBlocksDroped += 1
            if game.DropRate > 3000 and game.nrOfBlocksDroped % 5 == 0:
                game.DropRate -= 500
            DropBlock()


        # Then we Check if a Key is Pressed
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:      #Space Key
                if (target >= 0 and target < len(monster_list)):
                    #print("space",target)
                    monster_list.pop(target)
                    num_list.pop(target)
                    target = -1

            if ev.key == pygame.K_a:  #Left Key
                pygame.draw.rect(screen,alpha_light,[0,0,140,height])
                lp = True

            if ev.key == pygame.K_d:  #Right Key
                pygame.draw.rect(screen,alpha_light,[width-140,0,width,height])
                rp = True

            # när jag försökte göra detta med piltangenterna fuckar upp-tangenten ut när den kombineras med höger och vänster
            # men det funnkar med WASD så kör på det tills vidare
            if ev.key == pygame.K_w: # UP
                if lp == True:
                    if lnum > 1:
                        lnum -= 1
                    else:
                        lnum = 10
                    lb_Changed()
                if rp == True:
                    if rnum > 1:
                        rnum -= 1
                    else:
                        rnum = 10
                    rb_Changed()

            if ev.key == pygame.K_s: # DOWN
                if lp == True:
                    if lnum < 10:
                        lnum += 1
                    else:
                        lnum = 1
                    lb_Changed()
                if rp == True:
                    if rnum < 10:
                        rnum += 1
                    else:
                        rnum = 1
                    rb_Changed()
                        
        # Then we Check if a Key is Released
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_a:
                pygame.draw.rect(screen,dark,[0,0,140,height])
                lp = False
            if ev.key == pygame.K_d:
                pygame.draw.rect(screen,dark,[width-140,0,width,height])
                rp = False
              
        if ev.type == pygame.MOUSEBUTTONDOWN:        #Checks if a Mouse is clicked
            # Then we check where we clicked
            if 140 <= mouse[0] <= width-140 and 60 >= mouse[1]: #Debug prompt button
                pygame.quit()
                exit()

            if 0 <= mouse[0] <= 0+140: # Left panel
                lnum = getValue()
                leftnum = smallfont.render(str(lnum), True, white)
                resnum = smallfont.render(str(lnum * rnum), True, white) 
                  
            if width-140 <= mouse[0] <= width: # Right Panel
                rnum = getValue()
                rightnum = smallfont.render(str(rnum), True, white)
                resnum = smallfont.render(str(lnum * rnum), True, white) 
            
            if 140 <= mouse[0] <= width-140 and height-60 <= mouse[1]: # Result Button
                if (target >= 0 and target < len(monster_list)):
                    # print("space",target)
                    monster_list.pop(target)
                    num_list.pop(target)
                    target = -1

    pygame.draw.rect(screen,dark,[150,0,width-300,60])    # debug background
    pygame.draw.rect(screen,dark,[150,height-60,width-300,height])   # summary background
    pygame.draw.rect(screen,white,[canvas_x,canvas_y,canvas_w,canvas_h]) # the CANVAS
 
    # Draw All Buttons of the Side-Panels
    for y in range(10):
        # print(s(y),end=",")
        # print(str(y)+str(lnum)+str(rnum),end=",")
        yy = y * btn_h + 2
        #a if condition else b

        # Draw the highighting rectangles
        pygame.draw.rect(screen,light if lnum-1 == y else dark,[0,yy,btn_w,btn_h-gap])
        pygame.draw.rect(screen,light if rnum-1 == y else dark,[width-btn_w,yy,btn_w,btn_h-gap])

        txt1 = smallfont.render(str(y+1), True, white) 
        screen.blit(txt1 , (0+70,yy))
        screen.blit(txt1 , (width-70,yy))
        #print()

    # Skriver ut debugtexten
    screen.blit(debug_text, centerQuit)
    # Skriver ut Nummren på nedersta listen
    screen.blit(resnum , (width/2,height-50))
    screen.blit(leftnum , (width*0.25,height-50))
    screen.blit(rightnum , (width*0.75,height-50))
    
    # Move and Draw the "Enemies"
    v = [0,1]

    innerI = 0 # Index For Inside Below
    def EnemyMove():
        global innerI
        for rectangle in monster_list:
            # här gör vi valet om vi ska fortsätta att falla
            # så det är här vi behöver checka om vi har något under oss
            if rectangle.bottom < ((height - 60) - 60 * innerI):
                rectangle.move_ip(v)
            if innerI == target:
                pygame.draw.rect(screen, MIXED, rectangle)
            else:
                pygame.draw.rect(screen, RED, rectangle)
            movetext = smallfont.render(str(num_list[innerI]) , True , (0,0,0))
            centerText = movetext.get_rect(center=(rectangle.centerx,rectangle.centery))
            screen.blit(movetext , centerText)
            innerI += 1
    EnemyMove()

    # Ser Om Vi Har En lösning
    inI = 0 # Index For Inside Below
    #TargetSearch
    for num in num_list:
        foundOne = False
        #print(str(num) + " ",end="")
        if lnum * rnum == num:
            target = inI
            foundOne = True
            # print("Hittat "+str(target),end ="")
            break
        inI += 1
    if foundOne == False:
        target = -1
        # print("Inget Hittat")

    pygame.display.update()     # next frame
    debug_text = smallfont.render(str(game.nrOfBlocksDroped)+' quit '+str(game.DropRate)  , True , white)
    #print(lp,rp)
    clock.tick(60)#pygame.display.flip()
  
print("G A M E   O V E R")    
pygame.quit()