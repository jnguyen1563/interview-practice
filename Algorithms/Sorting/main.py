import numpy as np
from random import shuffle
import time

# import sorting algorithms
from algorithms.bubble_sort import standard_bubble_sort 

# Set consistent random seed
np.random.seed(9020)

# Create shuffled array
arr = np.arange(10)
shuffle(arr)

def timing_wrapper(func):
    def inner():
        start = time.time()
        print(start)
        func()
        end = time.time()
        print(end)
        elapsed_time = end-start
        print(f'Time elapsed: {elapsed_time:.10f}')
    return inner

@timing_wrapper
def main():
    standard_bubble_sort(arr)

if __name__ == '__main__':
    main()