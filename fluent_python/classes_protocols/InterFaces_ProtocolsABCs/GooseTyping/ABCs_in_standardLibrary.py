import array
from collections.abc import Hashable, Mapping, MutableSet, Sequence, Set
import random
infoMap = {'name':'Pranjal','Rollno':203033,'class':'Computer Science'}
unhashTuple = ('pranjal','joseph','elon',[1,2,3,4,5,6])
# print(hash(infoMap)),Throws TypeError: unhashable type: dict
# print(isinstance(unhashTuple,Hashable))

# Exploring the properties of standard python collections
from collections import abc

def goose_typing(c:abc.Collection)->list:
    _= lambda x : 'x' if x is True else ''
    # MutableSequence : list and tuples ,supports indexing and slicing
    # MutableMapping : like dict. associate values with keys, so we'll denote them as x["key"]
    # Sets support operations like intersections and difference,so we'll denote them as x & y
    mutable = (abc.MutableSequence,abc.MutableMapping,MutableSet)

    r = [
        c.__name__,
        _(issubclass(c,Sequence)),
        _(issubclass(c,Mapping)),
        _(issubclass(c,Set)),
        _(issubclass(c,mutable)),
        _(issubclass(c,Hashable)),
    ]

    return r


#  the function name, goose_typing,is not a mistake. this approach is indeed called goose typing,not duck typing

from rich.console import Console
from rich.table import Table
table = Table(title='Python Collections')
table.add_column('',justify='right',style='cyan',no_wrap=True)
table.add_column('x[0:]',justify='center')
table.add_column('x["key"]', justify='center')
table.add_column('x & y', justify='center')
table.add_column('mutable', justify='center')
table.add_column('hashable', justify='center')

for c in (array.array,list,tuple,dict,set,frozenset):
    table.add_row(*goose_typing(c))

d = dict()
table.add_row(*goose_typing(d.keys().__class__)) # dict_keys

"""
the result is interesting. the dict_keys object, returned by calling keys() on a dictionary,
behaves like a set, but is neither mutable or hashable.
"""
# d_collage = {'name':'Pranjal','RollNo':1203322,'age':20}

# d_school = {'name':'Joseph','RollNo':342211,'Age':23}

# matched_details = (d_collage.keys() & d_school.keys())

# FMT = "{}: {:>} | {:>}"
# for d in matched_details:
#     print(FMT.format(d,d_school[d],d_collage[d]))


# console = Console()
# console.print(table)

#  ------------------------------------------ Defining and using ABC -------------------------------------------------------

# here we create our Tombola ABC with two abstract and concrete method

import abc

class Tombola(abc.ABC):#1

    @abc.abstractmethod
    def load(self,iterable):#2
        """ Add items from an iterable """

    @abc.abstractmethod
    def pick(self):#3
        """
        remove item at random, and then return it.

        this method should raise `LookupError` when the instance is empty.
        """

    # Our concrete methods

    def loaded(self):#4

        """ return `True` if there's at least 1 item, `False` otherwise. """

        return bool(self.inspect()) #5
    
    def inspect(self):
        """Return a sorted tuple with items currently inside"""
        items = []
        while True:
            #6
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)#7
        return tuple(items)
    

# Explanation of above points
"""
1. To define an ABC,subclass abc.ABC.

2. An abstract method is marked with the @abstractmethod decorator, and often its body is empty except for a docstring.

3. The docstring instructs implementers to raise LookupError if there is no items to pick.

4. An ABC may include concrete methods.

5. Concrete methods in an ABC must rely on the interface defined by ABC.(i.e.,other concrete or abstract method or properties of the ABC).

6. We can't know how concrete subclasses will store the items, but we can build the
 inspect result by emptying the Tombola with successive calls to .pick()…

7. then use .load(…) to put everything back.
"""


# We now have our very own Tombola ABC. To witness the interface checking per-formed by an ABC,let's try to fool Tombola with a defective implementation.
# Example 13-8
# class Fake(Tombola): #1
#     def pick(self):
#         return 13
    
# print(Fake) # class was created. No problem so far
# f = Fake()
# print(f)


#  ------------------------------------------------------------------------ Subclassing an ABC -------------------------------------------------------------------------------

# developing two concrete subclasses 1.BingoCage 2.LotteryBlower

class BingoCage(Tombola):#1
    def __init__(self,items) -> None:
        self._randomizer = random.SystemRandom() #2
        self._items = []
        self.load(items)#3

    def load(self,items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items) #4

    def pick(self):#5
        try:
            return self._items.pop()

        except IndexError:
            raise LookupError('pick from empty bingo cage')
        
    def __call__(self):#6
        self.pick()

    """
    #1 This BingoCage class explicitly extends Tombola
    #2 using random.SystemRandom implements the random API on the top os.urandom(...) function,which provides the random bytes
    
    #3 Delegate initial loading
    """


# items = ["Pranjal","Mark","Tobey","Ahsley"]

# rr = random.SystemRandom()

# rr.shuffle(items)

# print(items)
