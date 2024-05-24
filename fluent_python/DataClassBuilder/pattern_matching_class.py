# There are three variations of the pattern matching class
# simple
# keyword
# and positional


# Simple class Pattern Matching
from dataclasses import dataclass
import typing

@dataclass
class Matches:
    long: int = 22.3
    lat: int = 44 # Fixed the syntax error here
    name: str = 'Japan'
    # here
    '''
    The simple pattern syntax of float(x) is a special case that applies only to nine
    blessed built-in types, listed at the end of the “Class Patterns” section of PEP 634—
    Structural Pattern Matching: Specification:
    bytes dict float frozenset int list set str tuple
    '''

    def match(self,ms):
        match ms:
            case float(ms):
                return f'Yes it matches to our data {self.name} coordintates = ({self.long},{self.lat})'
            


mat = Matches()
print(mat.match(list([22.3,44.2])))


# Keyword class Patterns

class City(typing.NamedTuple):
    continent:str
    city:str
    name:str

"""NOTE:
A data class is a regular Python class. The only thing that sets it apart is that it has basic data model methods like .__init__(), .__repr__(), and .__eq__() implemented for you.
"""

cities = [
 City('Asia', 'Tokyo', 'JP'),
 City('Asia', 'Delhi', 'IN'),
 City('North America', 'Mexico City', 'MX'),
 City('North America', 'New York', 'US'),
 City('South America', 'São Paulo', 'BR'),
]

def get_city_info(city):
    result = []
    match city:
        case City(continent = 'Asia'):
            result.append(f'{city.name} is in Asia')
            
    return result

def match_country_asian(cs):
    country = []
    match cs:
        case City(continent = 'Asia',city = cc):
            country.append(cc)
    
    return country
for i in cities:
    print(match_country_asian(i))
    
# Positional class Patterns

def match_american_cities():
    results = []
    for city in cities:
        match city:
            case City('North America',_,name):# here name is bound to the name of the city
                results.append(name)
                
    return results

print(City.__match_args__)