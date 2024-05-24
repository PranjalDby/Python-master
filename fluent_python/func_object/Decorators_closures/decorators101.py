"""  What is Decorators  """

""" A decorator is a callable that takes another function as argument (the decorated function). 
The decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object.

and vice versa.

More information on decorator:
1. A decorator is a function or another callable.
2. A decorator may replace the decorated function with different one
3. A decorator are executed immediately when a module is loaded.
"""

from typing import Any


def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print("Calling Target")

# example 9 :-

# focusing on point 3
# decorators are executed immediately when a module is loaded.

# registry = []

# def register(func): # executed immediately when a module is loaded.
#     print(f'running register({func})')
#     registry.append(func)
#     return func

# @register
# def f1():
#     print('running f1()')

# @register
# def f2():
#     print('running f2()')

# def f3():
#     print('running f3()')

# def main():
#     print('running main()')
#     print('registry ->',registry)
#     f1()
#     f2()
#     f3()

# if __name__ == '__main__':
#     main()

# Registration Decorators

""" How decorators are employed in real code or world. Basically there is two ways :"""

# The decorator function is defined in same module as the decorated function.
#  The register decorator returns the same function passed as argument. but most of decorator define an inner function and return it.


# Variable Scope Rules:

# Example 9-3: function reading a local variable and global

# If we want the interpreter to treat b as a global variable and still assign a new value to
# it within the function, we use the global declaration:
b = 30
def f1(a):
    global b
    print(a)
    print(b)
    b = 21

f1(34)
print(b)

# in above example : We Saw Two scopes in action:======
"""
1.The module global scope: made of names assigned at the top level of the module file.
2. The local scope: made of names assigned to value as parameters, or directly within a function body.
"""

"""                                                   CLOSURES                             """


# . And closures only matter when you have nested functions.

# Definiton: A closure is a function let's call it f -- with an extended scope that encompasses(Surrounded) variable refferenced in the body of 'f' that are not global or local variable of 'f'. such variable must come from the local scope of an outer function that encompasses 'f'.

# Example 9.7
class Averager:
    def __init__(self):
        self.series = []

    __prev_val = []
    def __call__(self,new_value):

        if len(self.series) == 0:
            self.series.append(new_value)
            return self.series[0]
        
        else:
            self.series.append(new_value)
            if len(self.__prev_val) == 0:
                total = sum(self.series)
                self.__prev_val.append(total)
            else:
                total = self.__prev_val[0] + self.series[-1]
                self.__prev_val[0] = total


            return total / len(self.series)
        
    
# Example 9.8 : a higher order function to calculate running average

def make_averager():
    # ----------------------------------------------------------------------------------------------
    series = [] # ???? 🤔🤔🤔🤔🤔Where the heck make_averager() is storing the series variable.  |
    def averager(new_value):                                                                       
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    
    # ----------------------------------------------------------------------------------------------
    # Closure
    
    return averager
avg  = make_averager() # Note that series is local variable of make_averager because assignment has been made inside the make_averager() function. but when avg(10) is called make_averager() has already returned, and its local scope is long gone. within averager,series is a free variable. This is a technical term meaning a variable that is not bound in the local scope.
print(avg(10))
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg(11))
print(avg(12))
print(avg(18))

# The value of series is stored in the __closure__ attribute of the returned function avg. Each item in avg.__closure__ corresponds to a name in avg.__code__.co_freevars. These items are cells, and they have an attribute cell_contents where the actual value can be found.

print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

#  The NonLocal Declaration
""" The nonlocal keyword lets you declare a variable as a free variable even when it assigned within the function. if a new value is assigned to a nonlocal variable, the binding stored in the closure is changed."""


# Example 9-13. Calculate a running average without keeping all history (fixed with the
# use of nonlocal)

def correct_make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count,total
        count += 1
        total += new_value
        return total / count

    return averager

avg = correct_make_averager()
print(avg(10))
print(avg(11))

# Variable lookup Logic

"""
When a function is defined, the Python bytecode compiler determines how to fetch a
variable x that appears in it, based on these rules:
1. if there is a global variable x declaration, x comes from and is assigned to the x global variable module.

2. if there is nonlocal x declaration, x comes from and is assigned to the local variable x in the nearest enclosing function. where x defined

3.if x is a parameter  or is assigned in the function body, it is local variable of the function.

4. if x is a refferenced but not assigned and not a parameter:
    — x will be looked up in the local scopes of the surrounding function bodies
    (nonlocal scopes)   
    — If not found in surrounding scopes, it will be read from the module global
    scope.
    — If not found in the global scope, it will be read from __builtins__.__dict__.
"""

# Simple Decorator implementation on decorator2.py file

