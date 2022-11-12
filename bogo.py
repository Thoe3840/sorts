from output import display_list
from random import shuffle
import pygame

def is_sorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True

def bogo_sort(a, w, h, disp):
    while not is_sorted(a):
        shuffle(a)
        display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
