from dataclasses import dataclass, field, fields
from collections import namedtuple
from math import asin, cos, radians, sin
from typing import List, Mapping
import unicodedata

@dataclass(order=True)
class PlayingCard:
    rank:str
    suit:str
    def __str__(self) -> str:
        return f'{self.suit} {self.rank}'

queen_of_hearts = PlayingCard('Q','Heart')
print(queen_of_hearts == PlayingCard('Q','Heart'))


# ------------------------------------ Regular Class Vs DataClass ---------------------------------------


# Regular class representation of above dataclass
# to add functionalities that a dataclass have on the box

class DataClassCard:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str: # added the functionality of print

        return (f'{self.__class__.__name__}('
                f'rank = {self.rank!r},suit = {self.suit!r})')
    
    #adding the functionality of compairing different instances of classes

    def __eq__(self,other) -> bool:
        
        if other.__class__ is not self.__class__:
            return NotImplemented

        return (self.rank,self.suit) == (other.rank,other.suit)
    


king_of_spade = DataClassCard("K","SPADE ♠️")

print(king_of_spade)

#! ----------------------------------------------- DataClass Alternative ---------------------------------------------------------------

NamedTupleCard = namedtuple('NamedTupleCard',['rank','suit'])

J_of_heart = NamedTupleCard("JOKER","HEART💘")

print(J_of_heart)

# By Design the namedtuple is just a regular tuple.
print(J_of_heart == ("JOKER","HEART💘"))

#! Warning ⚠️ subtle bugs ahead -----------------------------------------------------------

Person = namedtuple("Person",["first_initial","last_name"])

ace_of_spades = NamedTupleCard("A","SPades")

print(ace_of_spades == Person('A','SPades'))

#! Limitation of namedtuple is its nature is immutable
pp = Person("Pranjal","HELLOW")
# pp.first_initial = "KINGZAB"
# print(Person)

print("============================================================================================================================CX")


@dataclass
class Position:
    # this is same as
    """
    def __init__(self,name,lon,lat)
    """
    name:str
    lon:float = 0.0
    lat:float = 0.2
    # adding method to our dataclass
    def distance_to(self,other):
        r = 6731
        lam_1,lam_2 = radians(self.lon),radians(other.lon)
        phi_1,phi_2 = radians(self.lat),radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        

        return 2 * r * asin(h ** 1/2)


# we change the value of field in dataclass
# pos.lat = 23.22
# vanc = Position("vanc",-123.1,49.4)
# print(pos.distance_to(vanc))

#! --------------------------------------  More flexible dataclasses ----------------------------------------------



@dataclass
class Deck:
    cards:List[PlayingCard]

queen_of_hearts = PlayingCard('Q','Hearts')
ace_of_diamond = PlayingCard('A','ACE')


deck_two = Deck([queen_of_hearts,ace_of_diamond])


#! Advanced Default values ...........................................................................................

from unicodedata import *
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

SUIT = '♣ ♢ ♡ ♠'.split()

print("sss",SUIT[2] == "\N{WHITE HEART SUIT}")
def make_black_french_deck():
    return [PlayingCard(r,s) for s in SUIT for r in RANKS]


@dataclass(order=True)
class DeckWithDefaults:
    # Don't DO
    # cards:List[PlayingCard] = make_black_french_deck()
    name:str
    cards:List[PlayingCard] = field(default_factory=make_black_french_deck,metadata={"name":"Name of Dataclass","cards":"list of PlayingCard instances"})

    def __str__(self) -> str:
        cards = ", ".join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


dd = DeckWithDefaults("deck of black 1")

dd2 = DeckWithDefaults("deck of black 2")

# print(fields(DeckWithDefaults)[1].metadata['cards'])

#! --------------------------------- Adding Capability of Comparison to our PlayingCard dataclasses ------------------
queen_of_club = PlayingCard("Q","\N{WHITE CLUB SUIT}")
ace_of_diamond = PlayingCard('A',"\N{WHITE DIAMOND SUIT}")
joker_of_spade = PlayingCard('J',"\N{BLACK SPADE SUIT}")


#! ---- Modification 2

@dataclass(order=True)
class PlayingCardModified2:
    #this added as first becuase we want to do comparison according to this field
    sort_index:int = field(init=False,repr=False)
    rank:str
    suit:str

    # this method calls after __init__()
    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUIT) + SUIT.index(self.suit))
        
    def __str__(self) -> str:
        return f'{self.suit} {self.rank}'
queen_heart = PlayingCardModified2('Q','♡')
ace_spade = PlayingCardModified2('A','\N{BLACK SPADE SUIT}')


#!------------------------------------- Immutable Dataclasses -----------------------------------------------

@dataclass(frozen=True)
class ImmutablePosition:
    """This is a Frozen dataclass, you cannot assign values to the fields after creation"""
    name:str
    lat:float = 0.0
    lon:float = 0.0


# pos.name = 'stockholm' ! it will raise an DataClass.FrozenInstanceError

#! ---------------------------------- Inheritance ---------------------------------------------------------------------------
#! --- Class Capital extends Positions dataclass

@dataclass
class Capital(Position):
    country:str = 'Unknown'
    # this does not change the ordering of fields that are already defined in base classes
    lat:float = 40.0

#! ------------------------------------ Optimizing DataClasses --------------------------------------------------------------

@dataclass
class SimplePostions:
    name:str
    lon:float
    lat:float

@dataclass
class SlotsPosition:
    __slots__ = ("name","lon","lat")
    name:str
    lon:float
    lat:float


if __name__ == "__main__":
    print("Main Module")
    # capital = Capital("Oslo",20.3,54.9,"Norway") It will cause TypeError:non-default argument 'country' follows default argument
    # print(capital)

    # after defining country with its default value
    capital = Capital("Oslo",country="Norway")
    print(capital)

    simple = SimplePostions("London",-0.1,51.5)
    slot = SlotsPosition("Madrid",-3.5,45.5)
    