from output import display_list
import pygame

def partition(a, start, end):
    p = a[end]
    for i in range(start, end):
        if a[i] < p:
            a[start], a[i] = a[i], a[start]
            start += 1
    a[start], a[end] = p, a[start]
    return start

def quick_sort_(a, start, end, w, h, disp):
    part = partition(a, start, end)
    if part - start >= 2:
        if not quick_sort_(a, start, part-1, w, h, disp):
            return False
    if end - part >= 2:
        if not quick_sort_(a, part+1, end, w, h, disp):
            return False
    display_list(a, w, h, disp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def quick_sort(a, w, h, disp):
    return quick_sort_(a, 0, len(a)-1, w, h, disp)
