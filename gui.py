import pygame

"""
COLORS
"""

white = (255,255,255) # white white
light = (170,170,170) # light shade of the button
dark = (100,100,100) # dark shade of the button
alpha_light = (170,170,170,80) # dark shade of the button
GRAY = (155,155,155)
RED = (170,0,0)
MIXED = (150,0,150)



def setButtonsSize(var):
    global btn_h
    global btn_w
    btn_h = int(var) # Knappars höjd
    btn_w = int(140) # Knappars bredd
