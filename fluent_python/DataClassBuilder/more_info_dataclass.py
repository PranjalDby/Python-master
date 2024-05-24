from dataclasses import dataclass, field
from math import asin, cos, radians, sin, sqrt
import sys
from typing import List
from unicodedata import name
import dis
@dataclass
class Positions:
    name:str
    lat:float = 0.0
    long:float = 0.0

    def distance(self,other):
        r = 6371
        lam1, lam2 = radians(self.lat), radians(other.lat)
        phi1, phi2 = radians(self.long), radians(other.long)

        h = asin(sqrt(sin((lam2 - lam1) / 2) ** 2 + cos(lam1) * cos(lam2) * sin((phi2 - phi1) / 2) ** 2))

        return 2 * r * h
    

oslo = Positions('Oslo',59.95,10.75)
vancouver = Positions('Vancouver',49.25,-123.1)
oslo_vancouver_distance = oslo.distance(vancouver)
print(oslo_vancouver_distance)


# this is not recommended because it cause ValueError if you try to create a card with a rank or suit that is not in the list
# or if you delete some ranks or suits from the list it will also deleted from other instances of the class Deck


# recomended Way of Doing Above is to use field() function
# dataclasses uses default_factory to create a new list for each instance of Deck to handle the mutable default


@dataclass(order=True)
class PlayingCard:
    rank:str
    suit:str
    sort_index:int = field(init=False,repr=False)
    
    def __str__(self) -> str:
        return f'{self.suit}{self.rank}'
    
    def __eq__(self, __value: object) -> bool:
        
        if not isinstance(__value,PlayingCard):
            return False
        return self.suit == __value.suit and self.rank == __value.rank
    
    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit))

"""
@dataclass Parameters:
init: if true, a __init__() method will be generated. Default is True.

repr: if true, a __repr__() method will be generated. Default is True unless init is false.it contains class name and the name and repr of each field, in the order they are defined in the class.

eq: if true, an __eq__() method will be generated. Default is True. it compares the values of all fields, in the order they are defined in the class. If a field is a collection, the comparison is recursive. If a field is another dataclass, the comparison is recursive. If a field is a reference to a class that isn’t a dataclass, the comparison is by object identity.

order: if true, __lt__(), __le__(), __gt__(), and __ge__() methods will be generated. Default is False. it compares the values of all fields, in the order they are defined in the class. If a field is a collection, the comparison is recursive. If a field is another dataclass, the comparison is recursive. If a field is a reference to a class that isn’t a dataclass, the comparison is by object identity.

"""



"""WARNING """
# @dataclass
# class Deck:
#     cards:list[PlayingCard]

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r,s) for s in SUITS for r in RANKS]

@dataclass
class Deck:
    cards:List[PlayingCard] = field(default_factory=make_french_deck)
    
    def __repr__(self) -> str:
        print('WHy NOt Working')
        cards_ =  ', '.join(f'{card!s} ' for card in self.cards)
        
        return cards_

"""
Some Parameters of field() function:
1. default: if you want to set a default value for a field
2. default_factory: if you want to set a factory function to create a default value for a field
3. init: if you want to exclude a field from the __init__ method? default is True
4. repr: if you want to exclude a field from the repr method? default is True
5. compare: if you want to exclude a field from the comparison? default is True
6. hash: if you want to exclude a field from the hash calculation? default is to use the same as for compare
7. metadata: if you want to attach any arbitrary data to a field
"""
queen_of_hearts = PlayingCard('Q','♡')
ace_of_spades = PlayingCard('A','♠')

two_cards = Deck([queen_of_hearts,ace_of_spades])
print(RANKS)
print(len(RANKS))
print(len(SUITS))
print(RANKS.index(queen_of_hearts.rank) + SUITS.index(queen_of_hearts.suit))

print(queen_of_hearts > ace_of_spades)

