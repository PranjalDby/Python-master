"OPTIMIZING DATACLASS"
from dataclasses import dataclass
import pprint

@dataclass
class SimplerPosition:
    name:str
    lon:float
    lat:float
    
    
"""
@slots

object.__slots__
This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. __slots__ reserves space for the declared variables and prevents the automatic creation of __dict__ and __weakref__ for each instance.

"""

@dataclass
class SlotPosition:
    __slots__ = ['name','lon','lat']
    name:str
    lon:float
    lat:float
    

pprint()