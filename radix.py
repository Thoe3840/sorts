from output import display_list
from counting import counting_sort
import pygame

def radix_sort(a, w, h, disp):
    m = float('-inf')
    for x in a:
        if x > m:
            m = x
    p = 0
    while 10**p < m:
        if not counting_sort(a, w, h, disp, 10**p):
            return False
        p += 1
    return True
