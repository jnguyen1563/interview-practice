def merge_sort(arr):
    # Check to see if the arr is more than one element
    if len(arr) > 1:
        mid_idx = len(arr)//2

        # Split the array into left and right side
        left = arr[:mid_idx]
        right = arr[mid_idx:]

        # Recursively call merge sort on each side
        merge_sort(left)
        merge_sort(right)
        
        # Instantiate iteration variables
        # i -> left, j -> right, k -> overall array
        i = j = k = 0

        # Sort numbers from left and right split into overall array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # If left is less, sort it in
                arr[k] = left[i]
                i += 1
            else:
                # else if right is less, sort it in
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Sort any remaining entries into the overall array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr
