def standard_bubble_sort(arr):
    """ Standard bubble sort implementation """
    # Keep track of whether or not something was changed
    changed = True
    while changed: # Continue until nothing changes
        changed = False
        # Iterate over every element and look at the one behind it
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                # Swap if the previous number is greater
                arr[i-1], arr[i] = arr[i], arr[i-1]
                changed = True
    return arr