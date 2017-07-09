a = [9, 8, 3, 2, 6, 5, 7, 1, 10, 4]

def quick_sort(a):
    if len(a) <= 1:
        return a
    left_array = []
    right_array = []
    pivot = a[0]
    for element in a[1:len(a)]:
        if (element <= pivot):
            left_array.append(element)
        else:
            right_array.append(element)
    sorted_left = quick_sort(left_array)
    sorted_right = quick_sort(right_array)
    return attach_array(sorted_left, pivot, sorted_right)

def attach_array(sorted_left,pivot, sorted_right):  
    sorted_left.append(pivot)
    for element in sorted_right:
        sorted_left.append(element)
    return sorted_left
print(quick_sort(a))
