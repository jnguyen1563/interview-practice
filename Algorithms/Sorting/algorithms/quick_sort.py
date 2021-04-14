def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high-1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]