from output import display_list
import pygame

def gnome_sort(a, w, h, disp):
    i = 1
    r = 0
    while i < len(a):
        if not i or a[i] >= a[i-1]:
            i += 1
        else:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1

        r += 1
        if r >= 100:
            r = 0
            display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
