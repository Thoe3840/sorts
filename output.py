from pygame import *

BLACK = (0, 0, 0)
RED_GREEN = ((200, 0, 0), (0, 200, 0))

def display_list(a, h, disp):
    disp.fill(BLACK)
    for i, x in enumerate(a):
        rect = Rect(i, h - x, 1, x)
        draw.rect(disp, RED_GREEN[x == i], rect)
    display.update()
