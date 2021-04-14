import random
from random import shuffle
from timer import timing_wrapper

# import sorting algorithms
from algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort
# Set consistent random seed
random.seed(9020)

# Create shuffled list
lst = list(range(10))
shuffle(lst)
print(f'Shuffled list {lst}')

@timing_wrapper
def main():
    sorted = bubble_sort.standard_bubble_sort(lst)
    print(f'Sorted array: {sorted}')

if __name__ == '__main__':
    main()