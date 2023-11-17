# Copies are shallow by default

import copy


l1 = [3,[55,44],(7,8,9)]

l2 = list(l1) # shallow copy
"""
l2 bound  ->  l1[1]
l2 bound  ->  l1[2]
"""
# l2[0] = 33
print(l2 == l1) # True

print(l2 is l1) # False

l1.append(100) # it has no efttect on l2
l1[1].remove(55) # here we remove 55 from inner list of l1.This effects l2 also because l2[1] is bound to same list as l1[1]
print('l1:',l1)
print('l2:',l2)

l2[1] += [33,22] # this changes l1 also because l2[1] is bound to same list as l1[1] ,.. 
# For a mutable object like the list referred by l2[1], the operator += changes the
# list in place. This change is visible at l1[1], which is an alias for l2[1]
l2[2] += (10,11)
"""
+= on a tuple creates a new tuple and rebinds the variable l2[2] here. This is the
same as doing l2[2] = l2[2] + (10, 11). Now the tuples in the last position of
l1 and l2 are no longer the same object. 
"""

print('l1:',l1)
print('l2:',l2)

# Deep and shallow copy
# IN DEEP COPY, we copy the object and all the objects it refers to recursively,duplicates that do not share references of embedded objects

# IN SHALLOW COPY, we create a new container object and populate it with references to the child objects found in the original

class Bus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,remove):
        self.passengers.remove(remove)
    

bus1 = Bus(['Alice','Bill','Claire','David'])
bus2 = copy.copy(bus1) # shallow copy
bus3 = copy.deepcopy(bus1) # deep copy

print(id(bus1),id(bus2),id(bus3)) # different ids

bus1.drop('Bill')
print(bus2.passengers) # Bill is removed from bus2 also because bus2 is a shallow copy of bus1

print(bus3.passengers) # Bill is not removed from bus3 because bus3 is a deep copy of bus1

# Example representing Cyclic references:b refers to a and then appended to a

a = [10,20]
b = [a,30]
a.append(b)
print(a)

# function parameters as references
# The only mode of parameter passing in Python is call by sharing. That is the same mode used in Java, Ruby, and Scheme.

def f(a,b):
    a += b
    return a

# function may change any mutable object it receives
x = 1
y = 2
print(f(x,y)) # 3

a = [1,2]
b = [3,4]

print(f(a ,b))
print(a,b) # a is changed

t = (10,20)
u = (30,40)
print(f(t,u)) # (10,20,30,40) # tuple is immutable so a new tuple is created and returned

print(t)

# Mutable types as parameter defaults: bad idea

class HauntedBus:
    def __init__(self,passengers=[]):
        self.passengers = passengers
        
    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)
        
bus1 = HauntedBus(['Alice','Bill'])
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers) # ['Bill', 'Charlie']

bus2 = HauntedBus()
bus2.pick('Carrie')

bus3 = HauntedBus()
print(bus3.passengers) # ['Carrie']
bus3.passengers.append('Dave')
print(bus2.passengers) # ['Carrie', 'Dave'] # bus2 and bus3 share the same passengers list

# Here problem is bus2 and bus 3 share the same passengers list


class TwilightBus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)

# problem is that bus is aliasing the list that was passed as an argument to the constructor.
# instead, it should keep it own passengers list,as copy of passengers list

basketball_team = ['Sue','Tina','Maya','Diana','Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team) # ['Sue', 'Maya', 'Diana'] # basketball_team is changed

# Del and garbage collection
# object never explicitly destroyed; they may be garbage collected when no more references to them exist
# The first strange fact about del is that its not a function or keyword. Its a statement. we write del x and not del(x)
# the second fact is that del deletes the references or labels, not the objects themselves Python's garbage collector may discard an object from memory as an indirect result of del 

a = [1,2]
b = a
del a # del deletes the name a, not the object it was bound to
print(b) # b has no effects because b still points to it


# Example : Watching the end of an object when no more references to it exist

import weakref
s1 = {1,2,3}
s2 = s1
def bye():
    print('Gone with the wind...')
    
ender = weakref.finalize(s1,bye) # register bye callback on object s1
# Here Weakref to an object is used in order to donot increase the reference count of the object.therefore,it does not prevent the object from being garbage collected.

print(ender.alive) # True

# After del

del s1
print(ender.alive)
# s2 = 'spam'
print(ender.alive) # False