import pygame
import gamevars as g
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, g.DropRate)  # 

def setBtnSize(w,h):
    global btn_w
    global btn_h
    btn_w = w
    btn_h = h

def setWinSize(w,h):
    global width
    global height
    width = w
    height = h

def checkEvents():
    run = True # local variable with default value before all tests

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        #run = False # set local variable
        if ev.type == pygame.USEREVENT:
            pygame.time.set_timer(pygame.USEREVENT, g.DropRate)  # 
            g.nrOfBlocksDroped += 1
            if g.DropRate > 3000 and g.nrOfBlocksDroped % 5 == 0:
                g.DropRate -= 500
            return 'DROP_BLOCK'
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:  #Left Key
                return 'KEY_SPACE_PRESSED'
            if ev.key == pygame.K_a:  #Left Key
                return 'KEY_LEFT_PRESSED'
            if ev.key == pygame.K_d:  #Right Key
                return 'KEY_RIGHT_PRESSED'
            if ev.key == pygame.K_w: # UP
                return 'KEY_UP_PRESSED'
            if ev.key == pygame.K_s: # UP
                return 'KEY_DOWN_PRESSED'
            else:
                return 'UNUSED_KEY ' + str(ev.key) + ' PRESSED'
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_a:
                return 'KEY_UP_RELEASED'
            if ev.key == pygame.K_d:
                return 'KEY_DOWN_RELEASED'
        if ev.type == pygame.MOUSEBUTTONDOWN:        #Checks if a Mouse is clicked
            # Then we check where we clicked
            mouse = pygame.mouse.get_pos()
            if btn_w <= mouse[0] <= width-btn_w and btn_h >= mouse[1]: #Debug prompt button
                pygame.quit()
                exit()
            if 0 <= mouse[0] <= 0+btn_w: # Left panel
                return 'BTN_LEFT'
            if width-btn_w <= mouse[0] <= width: # Right Panel
                return 'BTN_RIGHT'
            if btn_w <= mouse[0] <= width-btn_w and height-btn_h <= mouse[1]: # Result Button
                return 'BTN_LAUNCH'

    # return run # return local value to main code