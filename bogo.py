from output import display_list
from random import shuffle

def is_sorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True

def bogo_sort(a, w, h, disp):
    while not is_sorted(a):
        shuffle(a)
        display_list(a, w, h, disp)
    display_list(a, w, h, disp)
