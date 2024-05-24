# In this session we see the uses of timeit module of python

from ast import stmt
import timeit

# this our setup code, hence executed only once before stmt.

setup_code = "from math import sqrt"

#this is our stmt code, and will executed as specified by parameter 'number'

stmt_code = "sum(sqrt(x) for x in range(1,10000))"

iterations = 10000

# time = timeit.timeit(stmt=stmt_code,setup=setup_code,number=iterations)

# print(time) #output is for 10000 iterations of code snippet and not a single iteration

# print(f'time taken for single iterations = {time / iterations}')


# Now We compare two sorting functions  one is our bubble sort and other is our built-in sorted functions


def getMeRandomArray(size):
    from random import randint

    return [randint(-100,100) for i in range(size)]

# print(getMeRandomArray(5))

def bubbleSort(array):
    if len(array) <=1:
        return array
    
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

    
    return array

test_array = getMeRandomArray(10)
def compare_functions(no_iterations):
    import timeit

    setup_code1 = """
from __main__ import bubbleSort
from __main__ import test_array
"""
    setup_code2 = """
from __main__ import test_array
"""
    stmt_1 = "bubbleSort(test_array)"
    stmt_2 = "sorted(test_array)"

    times_bubbleSort = timeit.repeat(stmt=stmt_1,setup=setup_code1,number=no_iterations)
    times_sorted = timeit.repeat(stmt=stmt_2,setup=setup_code2,number=no_iterations)
    print(f"Time taken by bubble sort is {min(times_bubbleSort)}")
    print(f"Time taken by built in sort is {min(times_sorted)}")


if __name__ == "__main__":
    compare_functions(10)

    
