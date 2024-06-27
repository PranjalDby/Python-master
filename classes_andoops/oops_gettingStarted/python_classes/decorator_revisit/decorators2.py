# Defining Decorators with optional Arguments

import functools


def repeat(no_times):
    #decorator factory
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for __ in range(no_times):
                value = func(*args, **kwargs)

            return value

        return wrapper

    return decorator_repeat


def repeat_modified(_func=None, *, no_times=4):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(no_times):
                value = func(*args, **kwargs)

            return value

        return wrapper

    if _func is None:
        """We called the decorator with arguments"""
        return decorator
    else:
        """ in this case,you called decorator without arguments,immediately apply the decorator to the function"""
        print("Directly Calling the decorator 🤫")
        return decorator(_func)



#----------------------------------------- Alternative ------------------------------------------
from functools import wraps,partial
import logging

def logged(func = None,*,level=logging.DEBUG,name = None,message=None):

    if func is None:
        # it returns a partial object that act as wrapper function
        return partial(logged,level=level,name=name,message=message)

    logname = name or func.__module__
    log = logging.getLogger(logname)
    logmsg = message or func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level,logmsg)
        return func(*args, **kwargs)

    return wrapper


#Example

@logged
def add(x,y):
    return x + y

@logged()
def subtract(x,y):
    return x - y

@logged(level=logging.CRITICAL,name="Example")
def spam():
    print("Spam Spam 🤮😡😡")



# tracking state in decorator
def track_state(func):
    functools.wraps(func) 
    def wrapper(*args,**kwargs):
        #adding a attribute to function
        wrapper.no_of_time += 1
        print(f"Call {wrapper.no_of_time} of {func.__name__}()")
        return func(*args,**kwargs)
    
    wrapper.no_of_time = 0

    return wrapper

@track_state
def shoutMe():
    import unicodedata

    print(f"Code Point {ord('🐭')}")
    print(f"Shouting BigMouse {unicodedata.lookup('MOUSE FACE')}")
    print(shoutMe.no_of_time)
   

class Counter:
    def __init__(self,start = 0):
        self.count = start

    # to make instance of class callable. implementing __call__()

    def __call__(self):
        self.count += 1
        print(f"Current Count is {self.count}")


class CountCalls:
    def __init__(self,func):
        functools.update_wrapper(self,func)
        """functools.update_wrapper(wrapper,wrapped) do is, make our wrapper function look like the wrapped functions by assigning the attributes of wrapped functions to itself"""
        self.func = func
        self.num_calls = 0

    def __call__(self,*args,**kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}()")
        return self.func(*args,**kwargs)
    
    
@CountCalls
def printMice():
    print('\N{MOUSE}')

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    # print(add(1,2))
    # print(subtract(10,2))

    # #!---- Another Example of Partial method

    # basetwo = partial(int,base = 2)
    # basetwo.__doc__ = 'Convert base 2 string to an int'
    # print(basetwo('10010'))

    # shoutMe() # shoutMe points at wrapper function and wrapper contains it original reference to shoutMe

    # ---------------------------------------- Using Classes as Decorators -----------------------------------------------------------------------
    printMice()
    printMice()
    print(globals())
    print(__name__)
    