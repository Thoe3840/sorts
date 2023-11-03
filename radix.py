from output import display_list
import pygame

def radix_sort(a, w, h, disp):
    m = float('-inf')
    for x in a:
        if x > m:
            m = x
    p = 0
    while 10**p < m:
        if not counting_sort_digit(a, 10**p, w, h, disp):
            print('quitting')
            return False
        p += 1
    return True

def counting_sort_digit(a, p, w, h, disp):
    c = [0]*10
    b = a.copy()

    for j in a:
        c[(j//p) % 10] += 1
    c[0] -= 1
    for j in range(1, 10):
        c[j] += c[j-1]
    for i in range(len(b)-1, -1, -1):
        x = b[i]
        d = (x//p) % 10
        a[c[d]] = x
        c[d] -= 1
        display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
