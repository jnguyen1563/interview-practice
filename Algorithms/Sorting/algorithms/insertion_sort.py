def insertion_sort(arr):
    """ Performs a basic insertion sort """
    # Iterate through every index beside the first
    for i in range(1, len(arr)):
        # Store the value of the current item
        curr_value = arr[i]

        # Get the index before the current
        prev_idx = i-1
        # Go backwards and check if the current value is less than
        # any of the previous
        while prev_idx >= 0 and curr_value < arr[prev_idx]:
            # Push every other value up in the index
            arr[prev_idx+1] = arr[prev_idx]
            prev_idx -= 1
        # Insert the current value into its appropriate place
        arr[prev_idx+1] = curr_value
    
    return arr