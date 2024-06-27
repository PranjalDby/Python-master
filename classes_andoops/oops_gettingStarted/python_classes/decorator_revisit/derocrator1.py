# function as first class objects

# functions can be assigned to variable like other objects

import functools
from re import U
import timeit
from typing import Any, Union


def square(a):
    return a ** 2


sqr = square

# print(sqr(23))

#! functions can be stored in data structers


def print_greet(greet):
    return greet

funcs = [square(i) for i in range(10)] #here square is called for every element

funcs1 = [print_greet,str.lower,str.upper]

# for func in funcs1:
#     print(func,func("Hello Pranjal"))
# # print(funcs)

#! functions can be passed to other functions as arguments

def greet(func):
    greeting = func("Hi, Iam VicenZo Cassano")
    print(greeting)


def greet_helpr(str):
    return f'💀💀💀 {str}... Nice to Meet You'


# higher order functions :e.g map

sqrt_ = map(lambda x: int(x ** (1/2)),funcs)



# --------------- Function Can Be nested ---------------------------------------------------------------

def whisper(text):
    def speak_also(t):
        return t.lower() + "Speaking ... 😊😊😊😊 "
    
    return f"{speak_also(text)}Don't Speak Just WHisper shuuuuh.....🤫🤫🤫🤫🤫🤫"



def get_speak_func(volume):
    def whisper(text):
        return f'{text.lower}......🤫🤫🤫'
    
    def yell(text):
        return text.upper() + '!'
    
    if volume > 0.5:
        #! returning function as object
        return yell
    
    else:
        return whisper


#! ---------- Functions Can Capture Local State ---------------------------------------------------


def get_speak_func_closure(text,volume):
    def whisper():
        return f'{text.lower}......🤫🤫🤫'
    
    def yell():
        return text.upper() + '!'
    
    if volume > 0.5:
        #! returning function as object
        return yell
    
    else:
        return whisper
    


def make_adder(n):
    def add(x):
        return x + n
    
    return add


#! objects can behave like Functions

class SquareRoot:
    def __init__(self,x):
        self.n = x

    """
    Behind the scenes, “calling” an object instance as a function attempts to execute the object’s __call__ method.
    """
    def __call__(self,number) -> Any:
        return (self.n ** (1/2)) * number
    

#! @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Decorators in Python @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def decorator(func):
    def wrapper():
        print("Something Happen'd before functions is called")
        func()
        print("After Function is Called.")

    return wrapper


def say_something():
    print("Hello i want to say something.....")



#! Example 2

from datetime import datetime
import functools
import timeit

# decorator factory
def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour <= 22:
            func()
            print("Decorating Function is called")
        else: pass # hush.... neighbours are asleep

    return wrapper


@not_during_the_night
def shout():
    print("AAAAAAAAaaaaaaaa.......RIIIIIIiiiiiiiiiiii.ttrrrr iam souting.....")


#! ------------------------------- Decorator that Accepts arguments ---------------------------------

def decorator_with_parameters(func):
    # to preserve information of oringinal func we have to use @functools.wraps()
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Calling Functions 📞📞📲")
        print(f'Name of Func = {func.__name__}')
        #! making decorator_function to return the value of decorated func
        res = func(*args,**kwargs)
        # if res:
        #     print(f'result of call = {res}')
        # else:
        #     ...
        return res

        

    return wrapper

@decorator_with_parameters
def adder(a,b):
    """ adder function adds two values"""
    return a + b


# print(ad_10_12)
# print(help(adder)) #it returns name of inner function wrapper instead of its name


#! ------------------------------------ Some real-world examples -------------------------------------------------------------------------

def decorators(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        #do something...
        value = func(*args,**kwargs)
        return value
    
    return wrapper_decorator


# above functions is good boilerplate for building more complex decorators

from sys import setrecursionlimit
import time
import timeit

# Timing Functions
def timer(func):

    """print the runtime for deocrated functions"""
    @functools.wraps(func)
    def timit_wrapper(*args,**kwargs):
        start_clock =  time.perf_counter_ns()
        call_func = func(*args,**kwargs)
        end_clock = time.perf_counter_ns()

        run_time = end_clock - start_clock

        #! in ms
        run_time = run_time / 1_000_000
        print(f'Finished {func.__name__}() in {run_time:.4f} milisec')

    return timit_wrapper

import gc
count = 0
def timer_timit(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        run_time = 0.0
        global count
        if count > 5:
            return run_time
        
        count +=1
        arr = []
        n = 0
        if args is not None:
            arr,n = args # Unpack the args tuple correctly

        else:
            arr = kwargs['arr']
            n = kwargs['n']
        stmt = f"{func.__name__}({arr},{n})"
        setup = "gc.enable();setrecursionlimit(5000)"
       
        run_time = timeit.timeit(stmt=stmt,setup=setup,timer=timeit.default_timer,globals = globals())
        
        return run_time

    return wrapper





@timer_timit
def bubble_sort(arr,n):
    #! bubble sort moves largest element to the end of array
    if arr == None:
        return 0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i] # moving largest element at the end of array

    return 1


def create_random_array(size):
    if size == 0:
        return []
    
    if size < 10000:

        import random
        
        __temp = []
        for i in range(size+1):
            rand_counter = random.randint(-10000,10001)
            __temp.append(rand_counter)

        
        return __temp
    
    return [0]



#! 000000000000000000000000000000000000000000 More Examples on Decorators @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#creating a debugger decorator

def debugger_deco(func):
    @functools.wraps(func)
    def wrappper_debug(*args,**kwargs):
        args_repr = [repr(s) for s in args]
        kwargs_repr = [f"{k}={repr(v)}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    
    return wrappper_debug


from typing import Optional,Callable

@debugger_deco
def greet(name, age: Optional[Union[int, str]] = None):
    
    if age is None:
        return f"Howdy {name}!"
    
    else:
        return f"Whoa {name}! {age} already, you're growing up!"
    

#Example : 2
import math

math.factorial = debugger_deco(math.factorial) # since we can't use the pie syntax to a builtin=func but we can directly apply decorator to it
def approximate_e(terms=18):
    return sum(1/math.factorial(n) for n in range(terms))

#Example : 3
def slow_down(func:Callable[[Optional[Union[int,str]],int],None]=None,sleep_counter = 1):
    """Sleep 1 sec before calling the function"""
    @functools.wraps(func)
    def inner_wrapper(*args,**kwergs):
        time.sleep(sleep_counter)
        print(func.__name__,func.__dir__)
        return func(*args,**kwergs)
    
    return inner_wrapper


@slow_down
def take_off_10s(parameter:Optional[Union[int,str]]=0,flag=10):

    if flag == 10:
        print("Launch Sequence initiated..\n")

    if flag < 1:
        print("Launch Done. 😎😎")

    if (parameter  == "launch" or parameter > 0) and flag > 0:
        print(f'Time Elapsed T-{flag} sec 🕛')
        take_off_10s(1,flag-1)

    
    

"""
REGISTERING PLUGINS
"""
PLUGINS= dict()

def register(func):
    """register func as plugins"""
    PLUGINS[func.__name__] = func

    return func


@register
def test_func1(name):
    return f"H'i There"

@register
def test_func2(name):
    return f"Yo {name}, together we're the awesome"


import random
def random_call(name):
    gg,gg1 = random.choice(list(PLUGINS.items()))
    print(f'Using {gg!r}')
    return gg1(name)

# Fancy Decorators === Decorating Class

class Circle:
    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        """Get Value of radius"""
        return self.__radius
    
    #property that have setter, it is compulsory to have setter same name as property
    @radius.setter
    def radius(self,value):
        if value >= 0:
            self.__radius = value
        
        else:
            raise ValueError("Value Must be +ve for radius property")
        
    
    @property
    def AREA(self):
        """Calculate the are of circle"""
        return self.pi() * self.radius ** 2
    
    def cylinder_volume(self,height):
        """Calculate volume of cylinder with circle as base"""
        return self.AREA * height
    
    @classmethod
    def unit_circle(cls):
        """Factory <Method> creating a circle with radius one"""
        return cls(1)
    
    @staticmethod
    def pi():
        return 3.14159


# ------- Nesting Decorators -----------------------------------------------------------

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        for i in range(2):
            res = func(*args,**kwargs)
        
    return wrapper

@debugger_deco
@do_twice
def greet(name):
    print(f'Hello {name}')

if __name__ == "__main__":
    # take_off_10s("launch")
    # print(PLUGINS)
    # print(random_call("Aliceeeeee"))
    
    # circle_radii_20 = Circle(20)
    # print(circle_radii_20.AREA) # this property is immutable, since it is property without .setter() method
    # # circle_radii_20.AREA = 1623.33; raises AttributeError: property 'AREA' of 'Circle' object has no setter

    # print(circle_radii_20.radius)# we can set the value of radius property since it has setter method associated with it.
    # circle_radii_20.radius = 30
    # print("After Changing the value of radius property = ",circle_radii_20.radius)

    greet("Pranjal Dubey")




