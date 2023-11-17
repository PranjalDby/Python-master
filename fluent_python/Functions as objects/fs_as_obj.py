# Anonymous functions: lambda

"""
The lambda keyword creates an anonymous function within a Python expression.
The lambda keyword is used to create anonymous functions.

NOTE::
lambda functions is pure expression. in other words, the body of lambda cannot make assignments or use any other Python statement such as while, try etc.

"""

# Example 7-7 Sorting a list of words by their reversed spelling using lambda function

fruits = ['strawberry', 'cherry', 'raspberry']
print(sorted(fruits,key=lambda word: word[::-1]))

# Fedrick Lundh, author of the ElementTree library, wrote a nice blog post about lambda:
# Write a comment explaining what the heck that lambda is for.
# Study a comment for while, and think of name that captures the essence of the comment
# convert the lambda to a def statement, and remove the comment

# The Nine flavours of callable objects

"""
1. User-defined functions: created with def statements or lambda expressions
2. Built-in functions: a function implemented in C (for CPython), like len or time.strftime
3. Built-in methods: methods implemented in C, like dict.get
4. Methods: functions defined in the body of a class
5. Classes: when invoked, a class runs its __new__ method to create an instance, then __init__ to initialize it, and finally the instance is returned to the caller. Because there is no new operator in Python, calling a class is like calling a function.
6. Class instances: if a class defines a __call__ method, then its instances may be invoked as functions.
7. Generator functions: functions or methods that use the yield keyword. When called, generator functions return a generator object.
8. Naive coroutine functions
"""

# User-Defined Callable Types
# not only are python functions real objects, but arbitrary python objects may also be made to behave like functions.

import random

class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()
    
bingo = BingoCage(range(2,10))
# print(bingo.pick())
# other-way around...

print(bingo())

# example 7-9: A Tag generates html elements; a keyword argument cls in the tag functions holds css class attributes as a dict


def tag(name,*content,class_ = None,**kwargs):
    """Generates one or more html tags"""
    
    if class_ is not None:
        kwargs['class'] = class_
    
    attrs_pairs = (f'{attr}="{value}"' for attr,value in sorted(kwargs.items()))
    attr_stair = ' '.join(attrs_pairs)
    if content:
        elements = (f'<{name} {attr_stair}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name} {attr_stair}/>'
    

# Note on keyword only arguments..
"""
Keyword-only arguments are a feature of Python 3. In Example 7-9, the class_
parameter can only be given as a keyword argument—it will never capture unnamed
positional arguments. To specify keyword-only arguments when defining a function,
name them after the argument prefixed with *. If you don’t want to support variable
positional arguments but still want keyword-only arguments, put a * by itself in the
signature, like this:

"""
def f(a,*,b):
    return a,b

print(f(1,b = 43))

# Positional-Only Parameters
    
"""
    def f(pos1,pos2,/,pos_or_kwd,*,kwd1,kwd2):
        -----------    ----------     ----------
            |             |                  |
            |        Positional or keyword   |
            |                                - Keyword only
             -- Positional only
    
    """

def divmod(a,b,/):
    return (a // b, a % b)

# NOTE: all arguments to the left of the / are positional-only.
print(divmod(20,8))