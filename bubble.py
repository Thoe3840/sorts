from output import display_list

def bubble_sort(a, w, h, disp):
    swapped = True
    i = len(a)
    while swapped and i > 0:
        i -= 1
        swapped = False
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        display_list(a, w, h, disp)
