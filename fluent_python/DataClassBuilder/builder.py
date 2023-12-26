"""
Python offers a few ways to build simple classes that is just collections of fields with little or no extra functionality.
That Pattern is Known as a Data Class.

this chapters covers three different class builders:
    - namedtuple
    - typig.NamedTuple
    - @dataclass.dataclass
"""

from collections import namedtuple

coordinate = namedtuple('Coordinate','lat Long')

print(issubclass(coordinate, tuple))


moscow = coordinate(55.75, 37.61)

print(moscow)

import typing
# The newer typing.NamedTuple provides the same functionality as namedtuple,adding type annotations to each field.

Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('long', float)])
print(typing.get_type_hints(Coordinate))


class Coordinates(typing.NamedTuple):
    lat: float
    long: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.long >= 0 else 'W'
        return f'{abs(self.lat):.1f} * {ns}, {abs(self.long):.1f} * {we}'
    

cr_india_kerla = Coordinates(10.85, 76.27)
print(cr_india_kerla)

# More on Classic Named Tuple

from collections import namedtuple

City = namedtuple('City',('name','country','population','coordinates'))

tokyo = City('Tokyo','JP',36.933,(35.689722,139.691667))
print(tokyo[1])

print(City._fields) # _fields is a tuple with the field names of the class
delhi = ('Delhi NCR','IN',21.935, Coordinates(28.613889,77.208889)) # _make() allow you to instantiate a named tuple from an iterable
delhi = City._make(delhi)# _asdict() returns a collections.OrderedDict built from the named tuple instance but after python 3.7 it returns a regular dict
print(delhi._asdict())

"""
since python 3.7, named tuple accepts the default keyword-only arguments providing an iterbale of N default values for each of the N RIGHTMOST parameters.

"""
library = namedtuple('Library','book_name id date_of_issue',defaults=['NA'])

university_library = library('Python',1234)

print(university_library)


# Hacking namedtuple to inject method

Card = namedtuple('Card','rank suit')
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
    
Card.suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(Card.suit_values) + Card.suit_values[card.suit]

Card.over_all_rank = spades_high

lowest_card = Card('2','clubs')
highest_card = Card('A','spades')
print(highest_card.over_all_rank())
