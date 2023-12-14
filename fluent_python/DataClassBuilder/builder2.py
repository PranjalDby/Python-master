# Initialization Variables That are not fields

"""
Sometimes we need to pass argument to the __init__ that are not instance fields.
Such arguments are called init-only variables and are defined in the __init_subclass__ method.
"""
# Important differences b/w data classes and typing.NamedTuple is dataclass contains mutable object as NamedTuple doesn't contain it
# 2. inheritance support
# 3. property decorators
from dataclasses import dataclass, InitVar, field, fields

# for Dublin Core Metadata Initiative example
from typing import Optional
from enum import Enum,auto
from datetime import date


class DataBase:
    def __init__(self,db_name:str):
        self.db_name = db_name
        self.db_list:dict = {}

    def populate(self,key,value):
        self.db_list[key] = value

    def lookup(self,key):
        if len(self.db_list) == 0:
            return None
        
        return self.db_list.get(key,None)
    
@dataclass
class C:
    i:int
    j:int = 0

    database:InitVar[DataBase | None] = None

    def __post_init__(self,database):
        self.db = database
        if self.j  is None and database is not None:
            self.j = database.lookup('j')

db = DataBase('my_db')
db.populate('a',100)
db.populate('b',245.22)
db.populate('c',92.33)
db.populate('j',30_000_000)
c = C(10,database=db)

print(fields(C))

# DublinCore Example

class ResourceType(Enum):
    BOOK = auto()
    eBOOK = auto()
    AUDIOBOOK = auto()
    VIDEO = auto()
    

@dataclass
class Resource:
    # Media resource description

    identifier:str
    title:str = '<Untitled>'
    creators:list[str] = field(default_factory=list)
    date:Optional[date] = None
    type:ResourceType = ResourceType.BOOK
    description:str = ''
    language:str = ''
    subjects:list[str] = field(default_factory=list)

    def __repr__(self) -> str:
        instance = self.__class__
        cls_name = instance.__name__
        res = [f'{cls_name}(']
        for i in fields(instance):
            value = getattr(self,i.name)
            res.append(f'{i.name}={value!r},')
        
        res.append(')')
        return '\n'.join(res)

description = 'This is a book about dataclasses'

book = Resource('978-1-789-870-54-9','Dataclasses in Python',['Jules Verne','H.G. Wells'],date(2021,8,1),ResourceType.BOOK,description,'en',['dataclasses','python','programming'])

print(book)