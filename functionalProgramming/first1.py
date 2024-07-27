from functools import reduce
from typing import Sequence, Union

# in python function are first-class citizens
def func():
    print("First Functions...")


# storing function as an object
ref = func
ref()

print("cat", 42, ref)

# we can store function inside a data structure
objects = ["cat", "dog", 343, ref]

print(objects)


# function compositions: when  call function from inside of another functions and pass function as parameter to other function.
def increment_func(a, b):
    return (a + 10, b + 10)


def sum(a, b, increment_func):
    # before sum we want to increase the value by 10;
    a, b = increment_func(a, b)

    return a + b


def sum_decorated(func):
    def wrapper(*args, **kwargs):
        print(f"entere'd arguments = {args} or kwargs = {kwargs}")
        a, b = func(*args, **kwargs)
        return a + b

    return wrapper


print(
    "sum of 10 and 20 after incrementing by 10 = ",
    sum_decorated(increment_func)(a=10, b=20),
)


# example of callback function

animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals,key= lambda x:x[-1])) # sorting based on the last character of string


# Defining an Anonymous Function with lambda.

reverse_s = lambda s: map(lambda x: x[:][::-1], s)
print("reversing string of list = ", list(reverse_s(animals)))
print("value returned by lambda expression are also callable", callable(reverse_s))
print(
    "value returned by lambda function may not be callable",
    callable(reverse_s(animals)),
)

# another example......
avg_lambda = lambda x, y, z: (x + y + z) / 3

print("Avg of three numbers = ", avg_lambda(2.3, 4.5, 6.7))

print("reversing elements in string according to length of items.")
print(sorted(animals, key=lambda s: len(s)))

tup = (1, 2, 3, 4, 5, [1, 2, 3, 4], {1: "Aryna", 2: "Hyena", 3: "tiger"})
li = [1, 2, 3]
t, *g = li
print(t, g)


def func(x):
    return x, x**2, x**3


print(func(30))

lambda_multiple = lambda x: [
    map(lambda x: x * 1, [x]),
    map(lambda p2: p2**2, [x]),
    map(lambda p3: p3**3, [x]),
]

convert_to_normal = lambda li: list(map(lambda p: list(p), li))

print(convert_to_normal(lambda_multiple(20)))

# python built-in map(<func>,<iterable>);

# using map to reverse the string

name = "Ellen Choi"

mp_obj = map(
    lambda s: s[-1] + "", name[::-1]
)  # it returns an iterator object which is called a map object


# or
for i in mp_obj:
    print(i, end="")

print("")

# reversing the elements of list

animals = ["cat", "dog", "hedgehog", "gecko"]

reverse_el = map(lambda e: e[::-1], animals)
print(list(reverse_el))

# join the element of list containig number

number = [1, 2, 3, 4, 5]

iterator = map(lambda n: str(n), number)

res = "+".join(list(iterator))

print(res)

# taking more than one iterables

# sum of elements of more than one iterable

sum = list(map(lambda x, y, z: (x + y + z), [1, 2, 3], [10, 20, 30], [100, 200, 300]))

print(sum)

# filtering an items based on conditions using filter method

# greater_than_100

res = filter(
    lambda x: x > 100, [1, 2, 78, 101, 111, 211]
)  # returns an filter object:which is an iterator
print(list(res))

# using filter to select only even numbers from the list
onlyEven = list(filter(lambda x:x % 2 == 0,[10,21,32,47,-1,5,2,7]))
print(onlyEven)

animals = ["cat", "dog", "hedgehog", "GECKO", "ferret", "vole", "tiger", "lion", "ELEPHANT", "GIRAFFE"]

print("only Uppercase animals = ",list(filter(lambda s:s.isupper(),animals)))

# -------------------------------------------------------------- reduce() ----------------------------------------------------------------

# Example:adding elements of list

elements = [1,2,3,4,5,6]
res = reduce(lambda x,y:x + y,elements)
print(res)
# Example 2: combine the string elements of list

combined_string = reduce(lambda x,y:x + y,['cat','dog','hedgehog','gecko'])
print(combined_string)

# Example 3: computing Factorials: n! = n * (n-1)


# n = int(input("Enter the n = "))
# fact = reduce(lambda x,y:x * y,range(n,0,-1))
# print(f"factorial of {n} is {fact}")


# Final Example: Finding the Maximum element in the list

maxx = [10,2,30,22,11,-1,2]
max_element = reduce(lambda a,b:a if a>b else b,maxx)

#  ------------------------------------------------------ reduce with initial value --------------------------------------------------------------

sum_with_100 = reduce(lambda x,y:x+y,[1,20,10,30,50],100)

print(sum_with_100)


# -------------------------------------- Implementing map() using reduce() ----------------------------------------------------------------------

def custom_map(func,iterable):
    return reduce(
        lambda x,y:x + [func(y)],
        iterable,
        []
    )


nums = [1,2,3,45,66]
ll = custom_map(str,nums);
print(ll[0])

ll2 = reduce(lambda x,y:x+[y],[1,2,34,55],[])

# def req(request:Sequence[Union[str,int,float],float]):
#         ...


# print(req())


# Note:

"""
To correctly use the format method in Python for the provided string, you should either use manual field specification for all placeholders or use automatic field numbering. Mixing both in a single format string is not allowed. Here's how you can correct the format method usage:

Option 1: Using Manual Field Specification:: field1   field2
print("Hello {0[0]} and {1[0]}".format("pranjal", ["friends"]))


Option 2: Using Automatic Field Numbering
print("Hello {} and {}".format("pranjal", ["friends"]))


In Option 1, {0[0]} refers to the first character of the first argument "pranjal", which is 'p', and {1[0]} refers to the first element of the second argument ["friends"], which is "friends".

In Option 2, {} placeholders are automatically numbered, so the first {} is replaced by the first argument "pranjal", and the second {} is replaced by the second argument ["friends"]. However, to access specific elements or characters, you would need to adjust the arguments passed to format accordingly, as automatic field numbering does not directly support indexing within the placeholder.
"""


# -------------------------------------------------------------------------------------------------------------------------------------#


# implementing custom filter using reduce

def custom_filter(func,iterable:Sequence):
    return reduce(
        lambda items,value: (items + [value]) if func(value) else items,
        iterable,
        []
    )



itr =[11,12,33,41,34,33,36,98]

fi = custom_filter(lambda x:x % 2 == 0,itr)

print(fi)