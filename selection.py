from output import display_list

def find_min(a, start):
    min = start
    for i in range(start, len(a)):
        if a[i] < a[min]:
            min = i
    return min

def selection_sort(a, w, h, disp):
    for i in range(len(a)):
        j = find_min(a, i)
        a[i], a[j] = a[j], a[i]
        display_list(a, w, h, disp)
