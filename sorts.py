import pygame
from pygame import *
import pyautogui
import math
from random import shuffle
from time import sleep

from output import display_list
from insert import insert_sort
from bubble import bubble_sort
from bogo import bogo_sort

pygame.init()

# set screen size to highest power of 2 below no. vertical pixels
WIDTH = HEIGHT = 2 ** math.floor(math.log(pyautogui.size()[1], 2))

DISP = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Sorts')

a = [i for i in range(1, WIDTH + 1)]
display_list(a, WIDTH, HEIGHT, DISP)

def new_sort(a, w, h, disp, sort_type, caption):
    display.set_caption(caption)
    shuffle(a)
    display_list(a, w, h, disp)
    sleep(1)
    sort_type(a, w, h, disp)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # change to buttons later
        elif event.type == KEYDOWN:
            if event.key == K_b:
                new_sort(a, WIDTH, HEIGHT, DISP, bubble_sort, 'Bubble Sort')
            elif event.key == K_i:
                new_sort(a, WIDTH, HEIGHT, DISP, insert_sort, 'Insert Sort')
            elif event.key == K_o:
                # pass in shorter list...
                new_sort([i for i in range(1, 8)], WIDTH, HEIGHT, DISP, bogo_sort, 'Bogo Sort')
