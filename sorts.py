import pygame
from pygame import *
import pyautogui
import math
from random import shuffle
from time import sleep

from output import display_list
from insert import insert_sort
from bubble import bubble_sort

pygame.init()

# set screen size to highest power of 2 below no. vertical pixels
WIDTH = HEIGHT = 2 ** math.floor(math.log(pyautogui.size()[1], 2))

DISP = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Sorts')

a = [i for i in range(WIDTH)]
display_list(a, HEIGHT, DISP)

running = True
while running:
    new_sort = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # change to buttons later
        elif event.type == KEYDOWN:
            if event.key == K_b:
                new_sort = True
                caption = 'Bubble Sort'
                sort_type = bubble_sort

            elif event.key == K_i:
                new_sort = True
                caption = 'Insert Sort'
                sort_type = insert_sort

            if new_sort:
                display.set_caption(caption)
                shuffle(a)
                display_list(a, HEIGHT, DISP)
                sleep(1)
                sort_type(a, HEIGHT, DISP)
