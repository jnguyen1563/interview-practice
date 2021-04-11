import numpy as np

def standard_bubble_sort(arr):
    """ Standard bubble sort implementation """
    changed = True
    while changed:
        changed = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                changed = True
    return arr