# Parameterized Generics and TypeVar

from collections.abc import Sequence,Hashable,Iterable
from typing import TypeVar
from random import shuffle
from collections import Counter
# TypeVar definition
T = TypeVar('T',int,str)
# Example
def sample(population:Sequence[T],size:int) -> list['T']:
    if size < 1:
        raise ValueError('size must be >= 1')
    
    result = list(population)
    shuffle(result)
    return result[:size]

# type Alias
t = tuple[int,...]

named:t = (1,2,3,4,6)
print(named)
res = sample("Pranjal is a Good Boy",len("Pranjal is a Good Boy"))
print(res)

# Bounded and restricted TypeVar()

# T_MOD = TypeVar('T_MOD',int,float,Fraction) # this specifies what type of variabe it accepts
# def mode(items:Iterable[T_MOD]) -> T_MOD:
#     pairs = Counter(items).most_common(1) # to -return single most common element from the iterable
#     if len(pairs) == 0:
#         raise ValueError('no Mode for Empty Data')
    
#     return pairs[0][0]
T_BOUNDED = TypeVar('T_BOUNDED',bound=Hashable)
def mode(items:Iterable[T_BOUNDED]) -> T_BOUNDED:
    pairs = Counter(items).most_common(1) # to -return single most common element from the iterable
    if len(pairs) == 0:
        raise ValueError('no Mode for Empty Data')
    
    return pairs[0][0]

result = mode([1, 1, 2, 3, 3, 3, 3, 4])
#res2 = mode([[1],[2],[2],[2],[3],[3]]) # error:TypeError unhashable type list

# Protocols from typing.protocols

def top(series:Iterable[T],length:int)->list[T]:
    ordered = sorted(series,reverse=True)
    return ordered[:length]

# print(top([4,1,5,2,6,7,3],3))

# but there is problem above and problem is how to constrain `T` it cannot be Any or Object, because the series must work with sorted. The sorted built-in actually accepts Iterable[Any], but that's Because the optional parameter key takes an arbritrary sort key from each element. What Happens if we Pass an Sorted List of Plain Objects but don't provide a key arguments.

l = [object() for _ in range(4)] 

#print(sorted(l)) # TypeError: '<' not supported between instances of 'object' and 'object'

# Another Quick- Experiment

# class Spam:
#     def __init__(self,n):
#         self.n = n

#     def __lt__(self,other):
#         #other is an another object of Same class
#         return self.n < other.n
    
#     def __str__(self)->str:
#         return f'Spam({self.n})'
    
# l = [Spam(n) for n in range(5,0,-1)]

# x = lambda elements : print(elements.n,end=" \n")

# for i in sorted(l):
#     x(i)

# That conforms it : I Can sort a list of Spam because Spam Implements __lt__ -- The Special Method that Supports < the operator

from typing import Protocol,Any
# This is an on the go interface
class SupportLessThan(Protocol):
    def __lt__(self,other:Any)->bool:
        ...

# A type `T` is 'consitent-with' a protocol `P` if `T` implements all the methods defined in P, with Matching type Signatures.

LT =TypeVar('LT',bound=SupportLessThan)
# Above intiution is that if LT is consitent with our protocol SupportLessThan if LT implements all the method defined in P, with Matching type Signatures

def modifiedTop(series:Iterable[LT],length:int)->list[LT]:
    ordered = sorted(series,reverse=True)
    return ordered[:length]

# Callabe from collections.abc
# Callablep[parameter_type = [zero or more paramter types],Return Type]
from collections.abc import Callable
# def repl(input_fun:Callable[[Any],str] = input) -> None: REPL stands for Read-Eval-Print-Loop

# Example 8-24: Variance in Callable types

def update(
        probe:Callable[[],float],
        display:Callable[[float],None]
)->None:
    temperature = probe()
    display(temperature)

def probe_ok():
     # probe_ok is consitent-with our Callable[[],float] because returning an int does not break code that expects a float
    return 42

def display_wrong(temperature:int) -> None:
    print(hex(temperature))

# update(probe_ok,display_wrong) # TypeError : becuase there is no gaurantee that a function that expects an int can handle float;for example,Python's hex functions accepts an int but rejects a float.
    
def display_ok(temperature:complex) -> None:
    print(temperature)

update(probe_ok,display_ok)

    

    


