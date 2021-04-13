import numpy as np
from random import shuffle
from timer import timing_wrapper

# import sorting algorithms
from algorithms import bubble_sort, selection_sort, insertion_sort
# Set consistent random seed
np.random.seed(9020)

# Create shuffled array
arr = np.arange(10)
shuffle(arr)

@timing_wrapper
def main():
    sorted = insertion_sort.insertion_sort(arr)
    print(sorted)
    
if __name__ == '__main__':
    main()