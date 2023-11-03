from output import display_list
from counting import counting_sort
import pygame
from math import log

def radix_sort_msd(a, w, h, disp):
    m = float('-inf')
    for x in a:
        if x > m:
            m = x
    p = int(log(m) // log(10))
    while p >= 0:
        if not counting_sort(a, w, h, disp, 10**p):
            return False
        p -= 1
    return True
