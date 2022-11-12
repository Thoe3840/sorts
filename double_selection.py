from output import display_list

def find_min_max(a, start):
    min = start
    max = start
    for i in range(start, len(a) - start):
        if a[i] < a[min]:
            min = i
        elif a[i] > a[max]:
            max = i
    return min, max

def double_selection_sort(a, w, h, disp):
    for i in range(len(a) // 2):
        j = -1*i - 1
        min, max = find_min_max(a, i)
        max_val = a[max]
        a[i], a[min] = a[min], a[i]
        if a[min] == max_val:
            a[j], a[min] = a[min], a[j]
        else:
            a[j], a[max] = a[max], a[j]
        display_list(a, w, h, disp)
