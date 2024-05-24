# implementing a single decorator
import functools
import time
def clock(func):
    def clocked(*args):
        print("Clocked Called")
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result}')
        return result

    return clocked
    

def modified_clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0 = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        print(f'[{elapsed:0.8f}s] {name}({args[0]}) -> {result}\n',end="\n")
        return result

    return clocked
@clock
def snooze(seconds:float):
    time.sleep(seconds)

@modified_clock
def fibonacci(n,memo):
    
    if n < 2:
        print(" ")
    if n < len(memo):
        return memo[n]

    else: 
        temp_fib = fibonacci(n-1,memo) + fibonacci(n-2,memo)
        memo.append(temp_fib)
        return temp_fib

@clock
def fibo(n):
    if n < 2:
        return n
    
    else:
        return fibo(n-1) + fibo(n-2)
    

# fibonnaci using caching from functool.cache

@functools.cache
@clock
def cached_fibo(n):
    if n < 2:
        return n
    else:
        return cached_fibo(n-1) + cached_fibo(n-2)
    
if __name__ == '__main__':

    # print("*" * 40, 'Calling snooze(.123)')
    # snooze(.123)
    # print("*" * 40, 'Calling fibonacci(6)')
    # print('6th fibonacci number is ',fibonacci(89,[0,1]))

    # here if we take factorial example the we see that the clock get the factorial function as its func argument: then it creates and returns the clocked function, then python interpreter binds to the factorial. so here factorial actually holds the refference to clocker func. from now on each time factorial(n) is called , clocked(n) will run

    # Example 9.16 uses the functools.wraps decorator to copy the relevant attributes from func to clocked.

    #------------------------------------Decorators in Standard Library -----------------------------------------------------------------#
    """
    Python has three built-in functions that are designed to decorate methods: property, classmethod, and staticmethod.
    In Example 9-16 we saw another important decorator: functools.wraps, a helper for building well-behaved decorators. some other decorators in the standard library are: lru_cache, singledispatch.
    """
    # Memoization with functools.cache
    # the functools.cache decorator implements memoization: an optimization technique that works by saving the results of previous invocations of an expensive function, avoiding repeat computations on previously used arguments.
    # print("*" * 40, 'Calling fibo(56)')
    # print(cached_fibo(56))
    # print(fibonacci(56,[0,1]))
    # Stacked Decorators
    """
    to make sense of stacked decorators,recall @ syntax is syntax sugar for applying the decorator function.
    if there is more than one decorator, they behave like nested functions
    # Example

    @alpha
    @beta
    def func():
        .....
    is same as:
    func = alpha(beta(func))
    in above the beta(func) is applied first, then the result of that is passed to alpha. so the order of decorators is important.
    """

    # Cheching order of decorators
    print(cached_fibo(30))
