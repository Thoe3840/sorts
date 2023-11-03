from pygame import *

BLACK = (0, 0, 0)
RED_GREEN = ((200, 0, 0), (0, 200, 0))

def display_list(a, w, h, disp):
    disp.fill(BLACK)
    breadth = w // len(a)
    length = h // max(a)
    #offset = min(a) breaks counting_sort
    offset = 1
    for i, x in enumerate(a):
        rect = Rect(i * breadth, h - x * length, breadth, length * x)
        draw.rect(disp, RED_GREEN[x == i + offset], rect)
    display.update()
