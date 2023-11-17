import timeit
from functools import *
# functions in python are first class objects.Programming languages researcher defines a "first class object" as a program entity that can be:
# 1. Created at runtime
# 2. Assigned to a variable or element in a data structure
# 3. Passed as an argument to a function
# 4. Returned as the result of a function


# Treating functions like Object


def factorial_naive(n):
    '''returns n!'''
    if n < 2:
        return 1
    return n * factorial_naive(n-1)

# doctest
# print(factorial.__doc__)
# # type of factorial

# print(type(factorial))

# # showing firstclass property of function
# fact = factorial
# print(fact(10,0))

# k = map(factorial,range(10))
# print(list(k))


# High-Order Functions

# A function that takes a function as argument or returns a function as result is a higher-order function.
# Example: map, filter

# Example: Sorting a list of words by length

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits,key=len)) # here we pass len as a function to key argument and then len function is applied to each element of fruits list


# Example: Sorting a list of words by their reversed spelling

def reverse(word):
    return word[::-1]

print(sorted(fruits,key=reverse))


# Modern replacement for map,filter and reduce

# Example 7-5 list of factorials produced with map and filter compared to alternative code as list comprehension

l_fact = list(map(factorial_naive,range(6)))
print(l_fact)
# print(factorial(5))
print("By Using List comprehensions...")
ls = [factorial_naive(x) for x in range(6)]
print(ls)

print()
print("By Using map and filter....")

l_map = list(map(factorial_naive,filter(lambda x: x % 2,range(6))))
print(l_map)

# the reduce function was demoted from built-in python 2 to the functools module in python 3
from operator import add

# reduce is used to apply a function to a sequence and reduce it to a single value, it is useful for performing some computation on a list and returning the result and also for producing a cumulative result.

rr = reduce(add,range(100))
print(rr)
