from output import display_list

def insert_sort(a, h, disp):
    for i, x in enumerate(a):
        j = i-1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        display_list(a, h, disp)
