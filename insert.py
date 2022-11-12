from output import display_list
import pygame

def insert_sort(a, w, h, disp):
    for i, x in enumerate(a):
        j = i-1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
