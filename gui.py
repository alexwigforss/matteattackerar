import pygame
pygame.init()                           # initializing the constructor

"""
COLORS
"""

white = (255,255,255) # white white
light = (170,170,170) # light shade of the button
dark = (100,100,100) # dark shade of the button
black = (0,0,0)
alpha_light = (170,170,170,80) # dark shade of the button

GRAY = (155,155,155)
RED = (170,0,0)
BLUE = (0,170,0)
MIXED = (150,0,150)

smallfont = pygame.font.SysFont('Corbel', 35)
xsmallfont = pygame.font.SysFont('Corbel', 16)
debug_text = smallfont.render('quit', True, white)
debug_text2 = xsmallfont.render('2', True, black)
txt1 = smallfont.render('1', True, white)

def debugdraw(s,g):
    pygame.draw.line(s, RED, (0,g), (width,g), 2)
    #pygame.draw.rect(s, BLUE, [150, 150, width-150, height-150],3)

def debugDistr(s,g,rd):
    c = 1
    for e in rd:
        pygame.draw.rect(s, BLUE, [150, g-btn_h*c, width-300, btn_h],3)
        c+=1
def updateDebugText(left,right):
    global debug_text
    # debug_text = smallfont.render(str(left) + ' quit ' + str(right), True, white)
    debug_text = smallfont.render(str(left) + ' q ' + str(right), True, white)
    return

def updateDebugText2(txt):
    global debug_text2
    # debug_text = smallfont.render(str(left) + ' quit ' + str(right), True, white)
    debug_text2 = xsmallfont.render(str(txt), True, black)
    return

def setButtonsSize(var):
    global btn_h, btn_w, mns_h
    btn_h = int(var) # Knappars höjd
    mns_h = int(var)
    btn_w = int(140) # Knappars bredd

def setWithHeight(w,h):
    global width
    global height
    width = w
    height = h

#   ╦ ╦┌─┐┌─┐┬  ┬┌─┐┬─┐  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐
#   ╠═╣│ ││ │└┐┌┘├┤ ├┬┘  ║  ├─┤├┤ │  ├┴┐└─┐
#   ╩ ╩└─┘└─┘ └┘ └─┘┴└─  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘

def lefty(mouse):
    global mouseoverLeft
    mouseoverLeft = getValue(mouse)
def righty(mouse):
    global mouseoverRight
    mouseoverRight = getValue(mouse)
def between():
    global mouseoverLeft
    global mouseoverRight
    mouseoverLeft = 0
    mouseoverRight = 0
mouse = pygame.mouse.get_pos()
def getValue(mouse):
    return int(mouse[1]/height*10+1)

def mouseHooverChecks(screen):
    global mouse
    once = True
    # stores the (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()
    # Quit Button
    if btn_w <= mouse[0] <= width-btn_w and btn_h >= mouse[1]:
        pygame.draw.rect(screen, light, [0+150, 0, width-300, btn_h])
    # Launch Button
    elif btn_w <= mouse[0] <= width-btn_w and height-btn_h <= mouse[1]:
        pygame.draw.rect(screen, light, [150, height-btn_h, width-300, height])
    # Left panel
    elif 0 <= mouse[0] <= 0+btn_w:
        pygame.draw.rect(screen, alpha_light, [0, 0, btn_w, height])
        once = True
        lefty(mouse)
    # Right panel
    elif width-btn_w <= mouse[0] <= width:
        pygame.draw.rect(screen, alpha_light, [width-btn_w, 0, width, height])
        once = True
        righty(mouse)
    else:
        # Rest of the area ie the canvas
        if once:
            pygame.draw.rect(screen, dark, [0, 0, btn_w, height])
            pygame.draw.rect(screen, dark, [width-btn_w, 0, width, height])
            once = False
    return