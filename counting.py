from output import display_list
import pygame

def counting_sort(a, w, h, disp, p = 0):
    if p:
        m = 10
        def f(x):
            return (x//p) % 10
    else:
        m = float('-inf')
        for x in a:
            if x > m:
                m = x
        def f(x):
            return x-1
    c = [0] * m
    b = a.copy()

    for j in a:
        c[f(j)] += 1
    c[0] -= 1
    for j in range(1, m):
        c[j] += c[j-1]
    for i in range(len(b)-1, -1, -1):
        x = b[i]
        a[c[f(x)]] = x
        c[f(x)] -= 1
        display_list(a, w, h, disp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    return True
