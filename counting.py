from output import display_list
import pygame

def counting_sort(a, w, h, disp):
    m = float('-inf')
    for x in a:
        if x > m:
            m = x
    c = [0] * m
    b = a.copy()

    for j in a:
        c[j-1] += 1
    c[0] -= 1
    for j in range(1, m):
        c[j] = c[j] + c[j-1]
    for i in range(len(b)-1, -1, -1):
        x = b[i]
        #print('{}: {}'.format(i, x))
        a[c[x-1]] = x
        c[x-1] -= 1
        display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
