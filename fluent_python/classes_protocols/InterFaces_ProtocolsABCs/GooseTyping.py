# Subclassing an ABC

# Example: 13-6. frenchdeck2.py: FrenchDeck2,a subclass of collections.MutableSequence

from collections import namedtuple,abc
import re

Card = namedtuple('Cards',['rank','suit'])

class FrenchDeck2(abc.MutableSequence):
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spade,diaomonds,club,heart'.split(',')

    def __init__(self) -> None:
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    
    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
    
    def __setitem__(self,position,value): #1
        self._cards[position] = value

    # def __delitem__(self,position): #2
    #     del self._cards[position]

    
    def insert(self,position,value): #3
        self._cards.insert(position,value)


# Meanings of Points Listed Above

"""
#1: __setitem__ is all we need to enable shuffling
#2: ... but subclassing MutableSequence forces us to implement __delitem__, an abstract method of an ABC
#3:  we are also required to implement insert, the third abstract method of MutableSequence

"""

fdeck = FrenchDeck2()