from output import display_list
import pygame

def max_heapify(a, i, l):
    left = i*2+1
    if left < l:
        if left + 1 < l:
            largest = [left, left + 1][int(a[left + 1] >= a[left])]
        else:
            largest = left
        if a[largest] > a[i]:
            a[largest], a[i] = a[i], a[largest]
            max_heapify(a, largest, l)

def build_max_heap(a):
    for i in range(len(a)//2 - 1, -1, -1):
        max_heapify(a, i, len(a))

def heap_sort(a, w, h, disp):
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        max_heapify(a, 0, i)
        display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
