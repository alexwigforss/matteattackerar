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
import helpers

# init window
clock = pygame.time.Clock()
pygame.init()# initializing the constructor
# res = (520,540) # Fönstrets storlek
res = (720,640) # Fönstrets storlek
screen = pygame.display.set_mode(res)# Öppnar Ett Fönster

# Timer För Hur Ofta Ett Nytt Block Introduceras
pygame.time.set_timer(pygame.USEREVENT, 10000)

# Färger  
color = (255,255,255) # white color
color_light = (170,170,170) # light shade of the button
color_dark = (100,100,100) # dark shade of the button
color_alpha_light = (170,170,170,80) # dark shade of the button
GRAY = (155,155,155)
RED = (170,0,0)
MIXED = (150,0,150)

# Sparar Fönstrets Dimensioner I Två Variabler
width = screen.get_width()
height = screen.get_height()

# Variabler för utdata av användarens val
num = lnum = rnum = 0
btn_h = int(height / 10)
tgleft = tgright = -1
gameOver = False
lp = rp = False
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
# rendering some texts written in this font
debug_text = smallfont.render('quit' , True , color)
centerQuit = debug_text.get_rect(center=(width/2,35))
txt1 = smallfont.render('1' , True , color)
resnum = smallfont.render(str(num), True, color) 
leftnum = smallfont.render(str(lnum), True, color) 
rightnum = smallfont.render(str(rnum), True, color) 
movetext = smallfont.render('0' , True , (0,0,0))

events = pygame.event.get() # For Key Detection

def lefty():
    mus = mouse[1]
    global mouseoverLeft
    mouseoverLeft = int(mus/height*10+1)
    # print("Hello from left",int(mus/height*10+1))

def righty():
    mus = mouse[1]
    global mouseoverRight
    mouseoverRight = int(mus/height*10+1)
    # print("Hello from right",int(mus/height*10+1))

def between():
    mus = mouse[1]
    global mouseoverLeft
    global mouseoverRight
    mouseoverLeft = 0
    mouseoverRight = 0

def getValue():
    return int(mouse[1]/height*10+1)

rectangle_list = [] # Enemy Factory 
num_list = []

def CreateEnemy():
    for r in range(0,1):
        rect = pygame.Rect(200, -100, width-400, 60)
        rectangle_list.append(rect)
        num_list.append(slumpfabrik.getRand())
        #print(num_list)
        if len(rectangle_list) > 10:
            global gameOver
            gameOver = True
CreateEnemy()

global target
target = -1

def lb_Changed():
    global leftnum,resnum
    leftnum = smallfont.render(str(lnum), True, color)
    resnum = smallfont.render(str(lnum * rnum), True, color) 

def rb_Changed():
    global rightnum,resnum
    rightnum = smallfont.render(str(rnum), True, color)
    resnum = smallfont.render(str(lnum * rnum), True, color) 

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
        pygame.draw.rect(screen,color_light,[0+150,0,width-300,60])
    # Launch Button
    elif 140 <= mouse[0] <= width-140 and height-60 <= mouse[1]:
        pygame.draw.rect(screen,color_light,[150,height-60,width-300,height])
    # Left panel
    elif 0 <= mouse[0] <= 0+140:
        pygame.draw.rect(screen,color_alpha_light,[0,0,140,height])
        once = True
        lefty()
    # Right panel
    elif width-140 <= mouse[0] <= width:
        pygame.draw.rect(screen,color_alpha_light,[width-140,0,width,height])
        once = True
        righty()
    else:
        # Rest of the area ie the canvas
        if once:
            pygame.draw.rect(screen,color_dark,[0,0,140,height])
            pygame.draw.rect(screen,color_dark,[width-140,0,width,height])
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
        if ev.type == pygame.USEREVENT:# Time to drop new block
            CreateEnemy()
        # Then we Check if a Key is Pressed
        if ev.type == pygame.KEYDOWN:

            if ev.key == pygame.K_SPACE:
                if (target >= 0 and target < len(rectangle_list)):
                    print("space",target)
                    rectangle_list.pop(target)
                    num_list.pop(target)
                    target = -1

            if ev.key == pygame.K_a:#Left
                pygame.draw.rect(screen,color_alpha_light,[0,0,140,height])
                lp = True

            if ev.key == pygame.K_d:#Right
                pygame.draw.rect(screen,color_alpha_light,[width-140,0,width,height])
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
                pygame.draw.rect(screen,color_dark,[0,0,140,height])
                lp = False
            if ev.key == pygame.K_d:
                pygame.draw.rect(screen,color_dark,[width-140,0,width,height])
                rp = False
              
        if ev.type == pygame.MOUSEBUTTONDOWN:        #Checks if a Mouse is clicked
            # Then we check where we clicked
            if 140 <= mouse[0] <= width-140 and 60 >= mouse[1]: #Debug prompt button
                pygame.quit()
                exit()

            if 0 <= mouse[0] <= 0+140: # Left panel
                lnum = getValue()
                leftnum = smallfont.render(str(lnum), True, color)
                resnum = smallfont.render(str(lnum * rnum), True, color) 
                  
            if width-140 <= mouse[0] <= width: # Right Panel
                rnum = getValue()
                rightnum = smallfont.render(str(rnum), True, color)
                resnum = smallfont.render(str(lnum * rnum), True, color) 
            
            if 140 <= mouse[0] <= width-140 and height-60 <= mouse[1]: # Result Button
                if (target >= 0 and target < len(rectangle_list)):
                    # print("space",target)
                    rectangle_list.pop(target)
                    num_list.pop(target)
                    target = -1


    pygame.draw.rect(screen,color_dark,[150,0,width-300,60])
    pygame.draw.rect(screen,color_dark,[150,height-60,width-300,height])
    pygame.draw.rect(screen,color,[150,60,width-300,height-120])

    #pygame.draw.rect(screen,color_dark,[0,0,140,height])
    #pygame.draw.rect(screen,color_dark,[width-140,0,width,height])

 
    # Draw All Buttons of the Side-Panels
    for y in range(10):
        # print(s(y),end=",")
        # print(str(y)+str(lnum)+str(rnum),end=",")
        yy = y * btn_h + 2
        #a if condition else b

        pygame.draw.rect(screen,color_light if lnum-1 == y else color_dark,[0,yy,140,60])
        pygame.draw.rect(screen,color_light if rnum-1 == y else color_dark,[width-140,yy,140,60])

        #pygame.draw.rect(screen,color_dark,[0,yy,140,60])
        #pygame.draw.rect(screen,color_dark,[width-140,yy,140,60])

        txt1 = smallfont.render(str(y+1), True, color) 
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
        for rectangle in rectangle_list:

            if rectangle.bottom < (height - 60) - 60 * innerI:
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
    debug_text = smallfont.render('quit' , True , color)
    #debug_text = smallfont.render(str(helpers.faktorer(num_list[0]) if len(num_list)>0 else ""), True , color)
    #debug_text = smallfont.render(str(target)+' quit '+str(num) , True , color)
    #print(lp,rp)
    clock.tick(60)#pygame.display.flip()
  
print("G A M E   O V E R")    
pygame.quit()