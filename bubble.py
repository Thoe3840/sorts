from output import display_list
import pygame

def bubble_sort(a, w, h, disp):
    swapped = True
    i = len(a)
    while swapped:
        i -= 1
        swapped = False
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
