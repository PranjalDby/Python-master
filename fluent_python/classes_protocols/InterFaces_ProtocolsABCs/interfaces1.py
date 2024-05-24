# Two Kinds of Protocols

#Example 13-1: Partial sequence protocol implementation with __getitem__

import collections
from random import shuffle
import re
from typing import Iterable, Iterator, Sequence, Union


class Vowels:

    def __getitem__(self,i):
        return 'AEIOU'[i]
    

v = Vowels()
print(v[:-1])

print('E' in v)


# A FrenchDeck example from chapter 1

Card = collections.namedtuple('Card',('rank','suit'))

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [
            Card(rank,suit) for suit in self.suits 
                       for rank in self.ranks]
        
    
    # Implementin sequence-protocol
        
    def __getitem__(self,pos):
        return self._cards[pos]
    
    def __len__(self):
        return len(self._cards)
    
    # implementing random.shuffle method
deck = FrenchDeck()

# print(shuffle(cd)) # it does not support item assignments, We can fix this by using MonkeyPatching

# This Whole Process is called dynamic duck typing....

def set_card(deck,position,card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card

shuffle(deck)
print(deck[:5])

# Example 13-5 : Duck typing to handle a string or an iterable of strings
def duckedNamedTuple(typeName:str,_fields:Union[str,Iterable[str]]):
    try:
        _fields = _fields.replace(","," ").split()
    
    except AttributeError:
        pass

    _fields = tuple(_fields)
    if not all(s.isidentifier() for s in _fields):
        raise ValueError("field_names must all be valid identifiers")
    
    else:
        return collections.namedtuple(typeName,_fields)
    

print (duckedNamedTuple("Ducked_named_tuple","Names Age Roll")._fields)

# Goose Typing : Focuses on ABCs..

#ABCs recognizing the class as an subclass with registering it.

# class Struggle:
#     def __len__(self):return 23



# from collections import abc

# print(issubclass(Struggle ,abc.Sized))


# Passing  A check like issubclass() we just register it with the suitable ABCs class

from collections.abc import Sequence

# Sequence.register(FrenchDeck)

# print(isinstance(FrenchDeck(),Sequence))
