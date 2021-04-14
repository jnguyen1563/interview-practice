def selection_sort(arr):
    # Loop through entire arr
    for i in range(len(arr)):
        curr_min_idx = i # The first element is assumed to be the least at first
        
        # Loop through the other numbers in the arr
        for j in range(i+1, len(arr)):
            # If a different number in the array is smaller, store its index
            if arr[j] < arr[curr_min_idx]:
                curr_min_idx = j
        
        # If a new minimum is found, swap it into the corresponding position
        if curr_min_idx != i:
            arr[i], arr[curr_min_idx] = arr[curr_min_idx], arr[i]

    return arr