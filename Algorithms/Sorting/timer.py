import time

def timing_wrapper(func):
    """ Wrapper function that computes the time another function takes to finish """
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f'Elapsed time: {(end-start):.8f}s')
    return inner