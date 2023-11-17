# Variables are labels, not boxes (or containers) in Python
"""
variable is a reference to an object, not the object itself (like a pointer in C) 
"""

"""Example 1 seeing that variable are labels not boxes"""

a = [1,2,3] # here a is referencing to the list object [1,2,3]
b = a # here we bind variable b to the same object that a is referencing to
a.append(4)
print(b)

# Therefore b = a statement does not copy the content of box a into box b.it attaches the label b to object that already has the label a attached to it

# Example 6-2. Variables are bound to objects only after the objects are created

class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))
        
x = Gizmo()
print(x)

"""
Identity,Equality and Aliases

Example 2. Charles and lewis refer to the same object
"""

charles = {'name':'Charles L. Dodgson','born':1832}

lewise = charles

print(lewise is charles)

print(id(charles),id(lewise))

lewise['balance'] = 950
print(charles)

"""Above We observe Following Things:
1.Lewis is alias for charles
2.lewise and charles are referencing to the same object
3.lewise and charles have same id
4.Adding an item to lewise is the same as adding an item to charles
"""

alex_imposter = {'name':'Charles L. Dodgson','born':1832,'balance':950}

print(alex_imposter == charles) # True. beacuse both have same content and we are comparing with values

print(alex_imposter is charles) # False. beacuse both are different objects and we are comparing with id


#                                                              Choosing between == and is


"""
The == operator compares the value of objects (the data they hold), while is compares their identities.

While Programming, we often care more about values than identities, so == appears more frequently than is in Python code.

However, when comparing a variable to a singleton, is is faster than ==, so you may see it in time-critical code that performs a lot of comparisons.

"""


# The Relative Immutability of tuples

"""Tuples, like most python collections,list,dict,sets,etc:are containers: they hold references to objects.
Immutability of tuples really refers to the physical contents of the tuple data structure (i.e., the references it holds), and does not extend to the referenced objects."""

# Example 3 id of item stored in tuple never changes

t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
print(t1 == t2) # True
print(id(t1[-1]))
t1[-1].append(99)
print(id(t1[-1]))   