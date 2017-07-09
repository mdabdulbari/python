from math import floor

a = [9, 8, 3, 2, 6, 5, 7, 4, 1, 10]

def merge_sort(a):
    if (len(a) == 1):
        return a
    mid = floor(len(a) / 2)
    b1 = merge_sort(a[0: mid])
    b2 = merge_sort(a[mid : len(a)])
    merged = merge(b1, b2)
    return merged


def merge(b1, b2):
    i = 0
    j = 0
    b = []
    while (i < len(b1) and j < len(b2)):
        if (b1[i] <= b2[j]):
            b.append(b1[i])
            i += 1
        
        else:
            b.append(b2[j])
            j += 1
    while (i < len(b1)):
        b.append(b1[i])
        i += 1

    while (j < len(b2)):
        b.append(b2[j])
        j += 1
    return b

print(merge_sort(a))
