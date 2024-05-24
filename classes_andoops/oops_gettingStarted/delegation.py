# Delegation is another technique that you can use as an alternative to inheritance.with delegation,you can model "can-do" relationships, where an object hand's task to another objects

class Stack:
    def __init__(self,items = None) -> None:
        if items == None:
            self._items = []

        else:
            self._items = list(items)

    def push(self,item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()
    

    def __str__(self):
        return f"{type(self).__name__} ({self._items})"
    
    def __repr__(self):
        return f"{type(self).__name__} ({self._items})"
    
# stack = Stack([1,2,3])

# print(stack)

# stack.push(32)
# print(f'after including an element {stack}')
# stack.pop()
# print(f'after removing an element {stack}')
# print(f'funtions that stack supports {stack.__dir__()}')
    

# -------------------------------------------- How to Quickly Implement delegation ----------------------------
    
import json
import pickle

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Serializer:
    def __init__(self,instance):
        pass