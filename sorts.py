import pygame
from pygame import *
import pyautogui
import math
from random import shuffle

pygame.init()

# set screen size to highest power of 2 below no. vertical pixels
WIDTH = HEIGHT = 2 ** math.floor(math.log(pyautogui.size()[1], 2))

DISP = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Sorts')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
