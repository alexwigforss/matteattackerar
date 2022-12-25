# DID ge rätt sorlek till rätt tal
# DID få dem att släppas i x-led där det finns plats
# TODO Få dem att falla till botten om det finns plats
# TODO cirkeldiagram ist fär att skriva ut fraktionerna med siffror
# TODO Test test test
# TODO Implementera problemz ist för slumpfabrik
import actions
import gui
import gamevars as g
import monsters
import slumpfabrik
from pygame.locals import *  # QUIT event needs this
import pygame
legend = """
 Instruktioner
 --------------------------------------------------------------------------
 Välj Siffror med musen
 När man har en match kan man spränga med space"""

run = True
# init window
clock = pygame.time.Clock()
pygame.init()                           # initializing the constructor
res = (720, 640)                         # Fönstrets storlek
screen = pygame.display.set_mode(res)   # Öppnar Ett Fönster

width = screen.get_width()
height = screen.get_height()
gui.setWithHeight(width,height)
actions.setWinSize(width, height)
centerQuit = gui.debug_text.get_rect(center=(width/2, 35))

# used for drawing the canvas and calcualate rows
actions.setBtnSize(140, 60)
gui.setButtonsSize(int(height / 10))
canvas_x = int(gui.btn_w + 10)
canvas_y = int(gui.btn_h)
canvas_w = int(width - canvas_x * 2)
canvas_h = int(height - canvas_y * 2)
# w_unit = canvas_w / 10
w_unit = canvas_w / 16
monsters.w_unit = canvas_w / 16
monstersizes = [3, 4, 6, 7, 10]
gap = int(5)

num = lnum = rnum = 0   # Variabler för utdata av användarens val
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

def getValue():
    return int(mouse[1]/height*10+1)

monster_list = []
list_of_rows_size = []
num_list = []

# Beroende på talets storlek tilldela Typ
def getSizeInd(nr):
    if nr < 11:
        si = 0
    elif nr < 31:
        si = 1
    elif nr < 51:
        si = 2
    elif nr < 71:
        si = 3
    else:
        si = 4
    return si

rowFilled = 0
rowsFilled = []
rowsDistr = []
def DropBlock():
    global rowFilled
    # TODO packa alla variabler här i en lista (eller tuple)
    # i objektet monster ist...
    #   dvs [numberis, sizeind, monster_w]
    numberis = slumpfabrik.getRand()
    sizeind = getSizeInd(numberis)
    monster_w = int(w_unit * monstersizes[sizeind])

    if rowFilled + monster_w > canvas_w:
        rowsFilled.append([[rowFilled],[True]])
        # print(rowsFilled)
        rowFilled = 0
        xpos = canvas_x
    else:
        xpos = canvas_x + rowFilled

    rowFilled = rowFilled + monster_w

    for r in range(0, 1):
        # TODO skapa en instans av monster här ist för rektangel.
        rect = pygame.Rect(xpos, -100, monster_w, gui.btn_h)
        monster_list.append(rect)
        num_list.append(numberis)
        if len(monster_list) > 30:
            # global g.gameOver
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


#    _  _  _  _____  _  ____     _         ___    ___   ____
#   | ||_|| |(____ || ||  _ \   | |       / _ \  / _ \ |  _ \
#   | |   | |/ ___ || || | | |  | |_____ | |_| || |_| || |_| |
#   |_|   |_|\_____||_||_| |_|  |_______) \___/  \___/ |  __/
#                                                      |_|
once = True
while g.gameOver == False:
        #   ╦ ╦┌─┐┌─┐┬  ┬┌─┐┬─┐  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐
        #   ╠═╣│ ││ │└┐┌┘├┤ ├┬┘  ║  ├─┤├┤ │  ├┴┐└─┐
        #   ╩ ╩└─┘└─┘ └┘ └─┘┴└─  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘
        # stores the (x,y) coordinates into the variable as a tuple
        mouse = pygame.mouse.get_pos()
        # Quit Button
        if gui.btn_w <= mouse[0] <= width-gui.btn_w and gui.btn_h >= mouse[1]:
            pygame.draw.rect(screen, gui.light, [0+150, 0, width-300, gui.btn_h])
        # Launch Button
        elif gui.btn_w <= mouse[0] <= width-gui.btn_w and height-gui.btn_h <= mouse[1]:
            pygame.draw.rect(screen, gui.light, [
                             150, height-gui.btn_h, width-300, height])
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
            pass
        #   ╔═╗╦  ╦╔═╗╔╗╔╔╦╗╔═╗
        #   ║╣ ╚╗╔╝║╣ ║║║ ║ ╚═╗
        #   ╚═╝ ╚╝ ╚═╝╝╚╝ ╩ ╚═╝
        e = actions.checkEvents()
        if e != None:
            # print(e)
            if e == 'DROP_BLOCK':
                DropBlock()
            if e.startswith('KEY'):
                if e == 'KEY_SPACE_PRESSED':
                    if (target >= 0 and target < len(monster_list)):
                        monster_list.pop(target)
                        num_list.pop(target)
                        target = -1
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
                    if (target >= 0 and target < len(monster_list)):
                        monster_list.pop(target)
                        num_list.pop(target)
                        target = -1

        # debug background
        pygame.draw.rect(screen, gui.dark, [150, 0, width-300, gui.btn_h])
        # summary background
        pygame.draw.rect(screen, gui.dark, [150, height-gui.btn_h, width-300, height])
        pygame.draw.rect(screen, gui.white, [canvas_x, canvas_y, canvas_w, canvas_h])  # the CANVAS

        # Draw All Buttons of the Side-Panels
        for y in range(10):
            yy = y * gui.btn_h + 2

            # Draw the highighting rectangles
            pygame.draw.rect(screen, gui.light if lnum-1 == y else gui.dark,[0, yy, gui.btn_w, gui.btn_h-gap])
            pygame.draw.rect(screen, gui.light if rnum-1 == y else gui.dark,[width-gui.btn_w, yy, gui.btn_w, gui.btn_h-gap])

            txt1 = gui.smallfont.render(str(y+1), True, gui.white)
            screen.blit(txt1, (0+70, yy))
            screen.blit(txt1, (width-70, yy))
            # print()

        # Skriver ut debugtexten
        screen.blit(gui.debug_text, centerQuit)
        # Skriver ut Nummren på nedersta listen
        screen.blit(resnum, (width/2, height-50))
        screen.blit(leftnum, (width*0.25, height-50))
        screen.blit(rightnum, (width*0.75, height-50))

        # Move and Draw the "Enemies"
        v = [0, 3]

        innerI = 0  # Index For Inside Below

        def EnemyMove():
            global innerI
            # global breakrow
            for rectangle in monster_list:
                # här gör vi valet om vi ska fortsätta att falla
                # så det är här vi behöver checka om vi har något under oss
                # BUG Just nu att rowsFilled läggs till när blocket skapas
                # ska det kunna falla flera samtidigt måste det ske när dem landat snarare
                # annars blir det luckor i mönstret
                # BUG 2 sedan ska de ju fortsätta falla när det blir tomt under
                # att poppa hela raden ur rowsfilled kan fixa men snyggare om
                # blocken kan "hitta" en lucka
                
                if rectangle.bottom < ((height - gui.btn_h) - gui.btn_h * len(rowsFilled)):
                    rectangle.move_ip(v)
                if innerI == target:
                    pygame.draw.rect(screen, gui.MIXED, rectangle)
                else:
                    pygame.draw.rect(screen, gui.RED, rectangle)
                movetext = gui.smallfont.render(str(num_list[innerI]), True, (0, 0, 0))
                centerText = movetext.get_rect(center=(rectangle.centerx, rectangle.centery))
                screen.blit(movetext, centerText)
                innerI += 1
        EnemyMove()

        # Ser Om Vi Har En lösning
        inI = 0  # Index For Inside Below
        # TargetSearch
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
        debug_text = gui.smallfont.render(str(g.nrOfBlocksDroped)+' quit '+str(g.DropRate), True, gui.white)
        clock.tick(60)  # pygame.display.flip()

print("G A M E   O V E R")
pygame.quit()
quit()