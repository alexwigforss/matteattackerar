# REFS  https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidelist
#       https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
#       https://www.geeksforgeeks.org/python-list-slicing/

#       Fold Everything     Ctrl+K , Ctrl+0
#       Print Without Newline   print(str(num) + " ",end="")

import os
import actions
import gui
import gamevars as g
import monsters as m
import slumpfabrik
from pygame.locals import *  # QUIT event needs this
import pygame

run = True
pygame.init()                           # initializing the constructor
clock = pygame.time.Clock()
res = (720,640) # Fönstrets storlek
screen = pygame.display.set_mode(res)   # Öppnar Ett Fönster
width = screen.get_width()
height = screen.get_height()
gui.setWithHeight(width,height)
actions.setWinSize(width, height)
centerQuit = gui.debug_text.get_rect(center=(width/2, 35))
center1 = gui.debug_text.get_rect(center=(width/2, 135))

# used for drawing the canvas and calcualate rows
actions.setBtnSize(140, 60)
gui.setButtonsSize(int(height / 10))
nrOfRows = 0
btn_x = int(gui.btn_w + 10)
btn_y = int(gui.btn_h)
canvas_w = int(width - btn_x * 2)
canvas_h = int(height - btn_y * 2)
m.w_unit = canvas_w / 16
gap = int(5)

num = lnum = rnum = 0   # Variabler för utdata av användarens val
#num = lnum = rnum = 1   # Vid Division för Kan inte dela med 0
enemy_x = gui.btn_w
lp = rp = False  # Leftpressed and RightPressed

# Resulting number of chosen factors
leftnum = gui.smallfont.render(str(lnum), True, gui.white)
rightnum = gui.smallfont.render(str(rnum), True, gui.white)
resnum = gui.smallfont.render(str(num), True, gui.white)
events = pygame.event.get()

# Where is the mouse cursor
def lefty():
    global mouseoverLeft
    mouseoverLeft = getValue()
def righty():
    global mouseoverRight
    mouseoverRight = getValue()
def between():
    global mouseoverLeft
    global mouseoverRight
    mouseoverLeft = 0
    mouseoverRight = 0
# global mouse
mouse = pygame.mouse.get_pos()
def getValue():
    return int(mouse[1]/height*10+1)
rect_list = []
list_of_rows_size = []
num_list = []
monsterList = []

rowFilled = 0
rowsFilled = []
rowDistr = []
rowsDistr = []

ground = height - gui.btn_h

def DropBlock():
    global rowFilled, rowsFilled, rowDistr, rowsDistr
    g.nrOfBlocksDroped += 1
    g.nrOfBlocks += 1
    monsterList.append(m.Monster(canvas_h,canvas_h,gui.btn_h))
    # Om monster + översta raden är bredare än canvas
    if rowFilled + monsterList[-1].width > canvas_w:
        rowDistr += canvas_w-rowFilled,False
        rowsDistr += [rowDistr]
        rowDistr = []
        rowsFilled.append([[rowFilled],[True]]) # Skapa ny rad
        rowFilled = 0   # Töm rowFilled
        xpos = btn_x
    else: # Annars om monster ryms på raden
        xpos = btn_x + rowFilled
    rowDistr += monsterList[-1].width,True
    rowFilled = rowFilled + monsterList[-1].width

    rect = pygame.Rect(xpos, -100, monsterList[-1].width, gui.btn_h)
    # rect = pygame.Rect(xpos, 0, monsterList[-1].width, gui.btn_h)
    rect_list.append(rect)
    num_list.append(monsterList[-1].numberis)
    if len(rowsFilled) > 8 :
        g.gameOver = True

DropBlock()

global target
target = -1

def lb_Changed():
    global leftnum, resnum
    leftnum = gui.smallfont.render(str(lnum), True, gui.white)
    resnum = gui.smallfont.render(str(lnum * rnum), True, gui.white)

def rb_Changed():
    global rightnum, resnum
    rightnum = gui.smallfont.render(str(rnum), True, gui.white)
    resnum = gui.smallfont.render(str(lnum * rnum), True, gui.white)

def cyclicInc(var, limit=10):
    if var < limit:
        var += 1
    else:
        var = 1
    return var

def cyclicDec(var, limit=10):
    if var > 1:
        var -= 1
    else:
        var = limit
    return var

def killer(t):
    global rect_list, num_list, rowsFilled, monsterList
    g.nrOfBlocks -= 1
    rect_list.pop(t)
    num_list.pop(t)
    monsterList.pop(t)
    search = 0
    for e in rowsDistr:
        for x in range(1, len(e)-1, 2):
            if e[x] == True:
                if search == t:
                    e[x] = False
                search += 1
    return target -1

def isEveryBoolFalse(row):
    blist = row[1::2]
    if True in blist:
        return False
    else:
        return True

"""def countTruesInDistr():
    global rowsDistr
    c = 0
    for item in rowsDistr:
        c += item.count(True)
    return c"""
    #   ╦ ╦┌─┐┌─┐┬  ┬┌─┐┬─┐  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐
    #   ╠═╣│ ││ │└┐┌┘├┤ ├┬┘  ║  ├─┤├┤ │  ├┴┐└─┐
    #   ╩ ╩└─┘└─┘ └┘ └─┘┴└─  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘
# gui.mouseHooverChecks(screen, mouse)

def mouseHooverChecks():
    # TODO  fixa varianten i gui
    global mouse,screen
    once = True
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
   
    # Quit Button
    if gui.btn_w <= mouse[0] <= width-gui.btn_w and gui.btn_h >= mouse[1]:
        pygame.draw.rect(screen, gui.light, [0+150, 0, width-300, gui.btn_h])
        #once = False
    # Launch Button
    elif gui.btn_w <= mouse[0] <= width-gui.btn_w and height-gui.btn_h <= mouse[1]:
        pygame.draw.rect(screen, gui.light, [150, height-gui.btn_h, width-300, height])
        #once = False
    # Left panel
    elif 0 <= mouse[0] <= 0+gui.btn_w:
        pygame.draw.rect(screen, gui.alpha_light, [0, 0, gui.btn_w, height])
        once = True
        lefty()
    # Right panel
    elif width-gui.btn_w <= mouse[0] <= width:
        pygame.draw.rect(screen, gui.alpha_light, [width-gui.btn_w, 0, width, height])
        once = True
        righty()
    else:
        # Rest of the area ie the canvas
        if once:
            pygame.draw.rect(screen, gui.dark, [0, 0, gui.btn_w, height])
            pygame.draw.rect(screen, gui.dark, [width-gui.btn_w, 0, width, height])
            once = False
    return

def grounded():
    return

#    _  _  _  _____  _  ____     _         ___    ___   ____
#   | ||_|| |(____ || ||  _ \   | |       / _ \  / _ \ |  _ \
#   | |   | |/ ___ || || | | |  | |_____ | |_| || |_| || |_| |
#   |_|   |_|\_____||_||_| |_|  |_______) \___/  \___/ |  __/
#                                                      |_|
while g.gameOver == False:
        
        # print(monsterList[0]) # Uncoment to show the first monster in list
        # gui.mouseHooverChecks(screen)
        mouseHooverChecks()
        #   ╔═╗╦  ╦╔═╗╔╗╔╔╦╗╔═╗
        #   ║╣ ╚╗╔╝║╣ ║║║ ║ ╚═╗
        #   ╚═╝ ╚╝ ╚═╝╝╚╝ ╩ ╚═╝
        e = actions.checkEvents()
        if e != None:
            if e == 'DROP_BLOCK':
                #if g.nrOfBlocks < 10:
                DropBlock()
            if e.startswith('KEY'):
                if e == 'KEY_P_PRESSED':
                    g.pauseSwap()
                    #print(g.paused)
                    #if not g.paused:
                    #    actions.timerOn
                    #else:
                    #    actions.timerOff
                if e == 'KEY_SPACE_PRESSED':
                    if (target >= 0 and target < len(rect_list)):
                        target = killer(target)
                if e == 'KEY_LEFT_PRESSED':
                    pygame.draw.rect(screen, gui.alpha_light,[0, 0, gui.btn_w, height])
                    lp = True
                if e == 'KEY_RIGHT_PRESSED':
                    pygame.draw.rect(screen, gui.alpha_light, [width-gui.btn_w, 0, width, height])
                    rp = True
                if e == 'KEY_UP_PRESSED':
                    if lp == True:
                        lnum = cyclicDec(lnum)
                        lb_Changed()
                    if rp == True:
                        rnum = cyclicDec(rnum)
                        rb_Changed()
                if e == 'KEY_DOWN_PRESSED':
                    if lp == True:
                        lnum = cyclicInc(lnum)
                        lb_Changed()
                    if rp == True:
                        rnum = cyclicInc(rnum)
                        rb_Changed()
                if e == 'KEY_UP_RELEASED':
                    pygame.draw.rect(screen, gui.dark, [0, 0, gui.btn_w, height])
                    lp = False
                if e == 'KEY_DOWN_RELEASED':
                    pygame.draw.rect(screen, gui.dark, [width-gui.btn_w, 0, width, height])
                    rp = False
            if e.startswith('BTN'):
                if e == 'BTN_LEFT':
                    lnum = getValue()
                    leftnum = gui.smallfont.render(str(lnum), True, gui.white)
                    resnum = gui.smallfont.render(str(lnum * rnum), True, gui.white)
                if e == 'BTN_RIGHT':
                    rnum = getValue()
                    rightnum = gui.smallfont.render(str(rnum), True, gui.white)
                    resnum = gui.smallfont.render(str(lnum * rnum), True, gui.white)
                if e == 'BTN_LAUNCH':
                    if (target >= 0 and target < len(rect_list)):
                        target = killer(target)

        # debug background
        pygame.draw.rect(screen, gui.dark, [150, 0, width-300, gui.btn_h])
        # summary background
        pygame.draw.rect(screen, gui.dark, [150, height-gui.btn_h, width-300, height])
        pygame.draw.rect(screen, gui.white, [btn_x, btn_y, canvas_w, canvas_h])  # the CANVAS

        # Draw All Buttons of the Side-Panels
        # TODO Move to GUI
        for y in range(10):
            yy = y * gui.btn_h + 2

            # Draw the highighting rectangles
            pygame.draw.rect(screen, gui.light if lnum-1 == y else gui.dark,[0, yy, gui.btn_w, gui.btn_h-gap])
            pygame.draw.rect(screen, gui.light if rnum-1 == y else gui.dark,[width-gui.btn_w, yy, gui.btn_w, gui.btn_h-gap])

            txt1 = gui.smallfont.render(str(y+1), True, gui.white)
            screen.blit(txt1, (0+70, yy))
            screen.blit(txt1, (width-70, yy))

#        ____ ____  ___    __  __ ___  ___ 
#       (  _ (  _ \/ __)  (  \/  / __)/ __)
#        )(_) ) _ ( (_-.   )    (\__ ( (_-.
#       (____(____/\___/  (_/\/\_(___/\___/
        def diBoogieng():
            # Skriver ut debugtexten
            msgLeft = mouse[0]
            msgRight = mouse[1]
            # msgLeft = str(g.nrOfBlocksDroped) +' '+ str(g.nrOfBlocks)
            # msgRight = str(target)
            gui.updateDebugText(msgLeft,msgRight)
            gui.updateDebugText2(rowFilled)
            centerQuit = gui.debug_text.get_rect(center=(width/2, 35))
            center1 = gui.debug_text2.get_rect(center=(width/2, 85))
            # Skriver ut debugtexter
            screen.blit(gui.debug_text, centerQuit,)
            screen.blit(gui.debug_text2, center1,)
            # Skriver ut Nummren på nedersta listen
            screen.blit(resnum, (width/2, height-50))
            screen.blit(leftnum, (width*0.4, height-50))
            screen.blit(rightnum, (width*0.6, height-50))
        diBoogieng()
        # Move and Draw the "Enemies"
        v = [0, 3]
        gv = [0, 2]
        l = [-1,0]
        r = [1,0]
        
        # mouserect = pygame.Rect([mouse[0],mouse[1], 100, 100])
        # pygame.draw.rect(screen, gui.BLUE, mouserect)  # the CANVAS

        innerI = 0  # Index For Inside Below

        def isOnRow(btm):
            global canvas_h
            inv_btm = abs(btm - canvas_h-10-gui.btn_h)
            row = int(inv_btm / gui.btn_h)
            return row+1

        def EnemyMove():
            global innerI
            for rectangle in rect_list:
                ghostrect = rectangle.move(gv)
                reslist = ghostrect.collidelistall(rect_list[0:innerI])
                if not g.paused:
                    if rectangle.bottom <= (height - gui.btn_h-1) and not reslist:
                        if not monsterList[innerI].newborn:
                            monsterList[innerI].out_of_index = True
                        monsterList[innerI].setRow(-1)
                        rectangle.move_ip(v)
                    else:
                        if monsterList[innerI].newborn:
                            monsterList[innerI].newborn = False
                        if monsterList[innerI].onRow < 0:
                            # Ist för rowsFilled bygg findrow
                            monsterList[innerI].setRow(isOnRow(rectangle.bottom))
                            #monsterList[innerI].setRow(len(rowsFilled)+1)
                if innerI == target:    # !!! Inner i must increse one per block. !!!
                    # Draw Worried Here
                    if monsterList[innerI].newborn:
                        pygame.draw.rect(screen, gui.MIXED, rectangle)
                    else:
                        pygame.draw.rect(screen, gui.MIXED, rectangle)
                else:
                    # Draw Regular here
                    if monsterList[innerI].newborn:
                        pygame.draw.rect(screen, gui.RED, rectangle,width=5)
                    elif monsterList[innerI].out_of_index:
                        pygame.draw.rect(screen, gui.YELO, rectangle,width=5)
                    else:
                        pygame.draw.rect(screen, gui.RED, rectangle,width=1)
                #mtext = str(num_list[innerI]) + ' ' + str(isOnRow(rectangle.bottom)) + ' ' + str(innerI)
                mtext = str(num_list[innerI]) + ' ' + str(monsterList[innerI].onRow) + ' ' + str(innerI)
                movetext = gui.smallfont.render(mtext, True, (0, 0, 0))
                #movetext = gui.smallfont.render(str(num_list[innerI]), True, (0, 0, 0))
                centerText = movetext.get_rect(center=(rectangle.centerx, rectangle.centery))
                screen.blit(movetext, centerText)
                innerI += 1

        EnemyMove()

        rowNr = 0
        for row in rowsDistr:
            if isEveryBoolFalse(row):
                rowsDistr.pop(rowNr)
                rowsFilled.pop(rowNr)
                ri = 0
                for monster in monsterList:
                    # monster.setRow(-1)
                    ri += 1
            rowNr +=1

        # row = 0
        gui.debugDistr(screen,ground,rowsDistr)
        # print(gui.btn_h) 
        gui.debugdraw(screen,ground)

        # Ser Om Vi Har En lösning
        inI = 0  # Index For Inside Below
        # TargetSearch
        for num in num_list:
            foundOne = False
            if lnum * rnum == num:
            #if lnum / rnum == num:
                target = inI
                foundOne = True
                break
            inI += 1
        if foundOne == False:
            target = -1

        if not g.paused:
            pygame.display.update()     # next frame
            clock.tick(60)              # pygame.display.flip()

print("G A M E   O V E R")
#import menu
pygame.quit()
quit()