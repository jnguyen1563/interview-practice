import numpy as np
from random import shuffle
from timeit import timeit

# import sorting algorithms
from Algorithms.Sorting.bubble_sort import bubble_sort

# Set consistent random seed
np.random.seed(9020)

# Create shuffled array
arr = np.arange(10)
np.random.shuffle(arr)


def sort(arr:list, algorithm='bubble'):
    return bubble_sort(arr)

def main():
    timeit(bubble_sort(arr), number=10)

if __name__ == '__main__':
    main()