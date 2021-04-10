import numpy as np

def bubble_sort(array):
    """ Standard bubble sort algorithm """
    changed = True
    # continue until changes stop being made
    while changed:
        changed = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                changed = True
    
    return array