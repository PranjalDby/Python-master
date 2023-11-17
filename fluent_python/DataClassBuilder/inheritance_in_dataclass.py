"""
@doc 
Inheritance in dataclass
"""
from dataclasses import dataclass,field

# @dataclass
# class Position:
#     name:str
#     lon:float = 0.0
#     lat:float = 0.0
# This will cause TyperError 'non-default argument 'country' follows default argument' because Position class has default arguments
# it creates __init__(name:str,lon:float = 0.0,lat:float = 0.0,country:str) method which is not valid in python

# Aware OF:
"""
How fields are ordered in subclass.
Starting With the base class,fields are ordered by the order in which they appear in the class definition.
If a field is redefined in a subclass, its order does not change.
ex = 
"""
    
@dataclass
class Position:
    name:str
    lon:float = 0.0
    lat:float = 0.0
    
    
@dataclass
class Capital(Position):
    country:str = "Unknown"
    lat:float = 40.0

cap = Capital('Oslo',country='Norway')

print(cap)