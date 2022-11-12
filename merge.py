from output import display_list

def merge(a, b, c, s):
    i = j = 0
    for k in range(s, len(b) + len(c) + s):
        if i >= len(b):
            a[k] = c[j]
            j += 1
        elif j >= len(c):
            a[k] = b[i]
            i += 1
        elif c[j] < b[i]:
            a[k] = c[j]
            j += 1
        else:
            a[k] = b[i]
            i += 1

def merge_sort_(a, s1, e1, s2, e2, w, h, disp):
    if s1 + 1 < e1 or s2 + 1 < e2:
        m1, m2 = (e1 - s1)//2 + s1, (e2 - s2)//2 + s2
        merge_sort_(a, s1, m1, m1, e1, w, h, disp)
        merge_sort_(a, s2, m2, m2, e2, w, h, disp)
    merge(a, a[s1 : e1], a[s2 : e2], s1)
    display_list(a, w, h, disp)

def merge_sort(a, w, h, disp):
    merge_sort_(a, 0, len(a)//2, len(a)//2, len(a), w, h, disp)
