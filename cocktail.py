from output import display_list
import pygame

def cocktail_sort(a, w, h, disp):
    start, end, dir = 0, len(a) - 1, 1
    swapped = True
    while swapped:
        swapped = False
        for j in range(start, end, dir):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        display_list(a, w, h, disp)
        start, end, dir = end - 2*dir, start - dir, -1*dir

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
