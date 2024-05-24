# A Vector2D class we see in previous Chapter,embrace with different methods
import array,math
# class Vector2D:
#     typecode = 'd'
#     def __init__(self,x,y):
#         self.x = float(x)
#         self.y = float(y)
    
#     def __iter__(self):
#         return (i for i in (self.x,self.y))
    
#     def __repr__(self) -> str:
#         class_name = type(self).__name__
#         return '{}({!r},{!r})'.format(class_name,*self)
    
#     def __str__(self) -> str:
#         return "Called __str__ "+str(tuple(self))
    

#     def __bytes__(self):
#         return (bytes([ord(self.typecode)]) + 
#                 bytes(array.array(self.typecode,self)))
    
#     def __eq__(self, __value: object) -> bool:
#         return tuple(self) == tuple(__value)
    
#     def __abs__(self):
#         return math.hypot(self.x,self.y)
    
#     # A_c1 
#     @classmethod
#     def frombytes(cls,octets):
#         typecode = chr(octets[0])
#         print(typecode)
#         memv = memoryview(octets[1:]).cast(typecode)
#         # changing the value
#         return cls(*memv) 


# An alternative Constructor:
# We have to still create a method that rebuilt our Vector2D from bytes
# Verifying each special methods
# v1 = Vector2D(3,4)
# x,y = v1 # this call __iter__() method,basically unpacking
# print(y)
# v1_clone = eval((repr(v1)))
# print(v1 == v1_clone) # comparison
# octets = bytes(v1) #here it uses the __bytes__ methods to produce a binary representation
# recreated_vector = v1.frombytes(octets)
# print(type(recreated_vector))

# memoryview() is applied only to that objects that supports buffer protocol.buit-in objects that support buffer protocol are bytes,bytearray
# random_byte_arr = bytearray('ABC','utf-8')
# print(random_byte_arr)
# memv = memoryview(random_byte_arr)
# memv[0] = 68
# print(memv.tolist()) 
# print(random_byte_arr)

#  ----------------- classmethod Versus staticmethod ------------------------------------------------------------

# class Method that operates on the class not on instance. class methods changes the way the method is called, so it receives the class itself as the first argument,instead of an instance its most common use is for alternative constructor,like frombytes class method.on last example it uses the cls argument by invoking it to build new instances: cls(*memv)
# staticmethod decorator: staticmethod decorator changes a method so that it receives no special first-argument.In essence the  staticmethod is just like a plain functions that happen to lie inside our class body, instead of being defined at the module level

# Example 11-4 compairing behaviours of classmethod and staticmethod

class Demo:
    @classmethod
    def klassMeth(*args):
        return args
    
    @staticmethod
    def statikmethod(*args):
        return args


# some more examples of class methods and instance methods
class Demo2:
    name = 'Demo2' #class attributes
    # instance method
    def instanceMethod(self,*args):
        print('Passed arguments are = {} with class attribute {}'.format(args,self.name))
    
    # classmethod
    @classmethod
    def classMethod(cls,*args):
        print('It is a Class Method')
        print(f'arguments you passed are {args} + {cls}')

    # static method : static method didn't take object-instance or cls as first parameters
    @staticmethod
    def staticMethod(*args):
        print('Its a Just normal functions')
        print('Arguments are = {!r}'.format(args))
    


# dm1 = Demo2()
#manual passing the instance of object instance
# dm1.instanceMethod(dm1,'Hello Instance Method')
# calling instanceMethod without creating instance method
# Demo2.instanceMethod() throws error TypeError: Demo2.instanceMethod() missing 1 required positional argument: 'self'
# Demo2().classMethod('MagicShop- Maxce')
# dm1.staticMethod('staticmethod calling')

# demo = Demo()
# ss = demo.klassMeth('pranjal') # it recieves the classname as the first argument
# # proof: (<class '__main__.Demo'>, 'pranjal')
# #invoking our staticmethod which is just a old function745
# normal_meth = demo.statikmethod('pranjal','johnson')

class Pizza:
    def __init__(self,ingredients,radius):
        self.ingredients = ingredients
        self.radius = radius
    
    def __str__(self) -> str:
        return f'Pizza({self.radius!r},{self.ingredients!r})'
    
    # adding some pizza factories with @classmethod
    """
    Below We create different pizza factories method that already have instruction according to factory type.
    this is useful when we decide to rename the class. so we don't have to remember updating the constructor
    name.

    @ one other important use of classmethod is that they will allow you to define alternative constructor for your classes.
    """
    @classmethod
    def mozarrella(cls):
        return cls(['mozzarella','tomatoes'],34.2)
    
    @classmethod
    def proscuitto(cls):
        return cls(['mozzarella','tomatoes','ham'],25.3)
    
    #staticmethod
    def circle_area(r):
        return math.pi * r**2

# ss = Pizza.mozarrella()
# print(ss)
#  ------------------------------------ Formated Displays ------------------------------------
"""
the f-string, the format() built-in function, and the str.format() method delegate the actual formmating to each type by calling their .__format__(format_spec) method.
1.The second argument in format(my_obj,format_spec), or
2.whatever appears after the colon in replacement field delimited with {} inside
an f-string or the fmt in the fmt.str.format()
"""
# example:-

# brl = 1 / 4.82 
# print(brl)
# formatted = format(brl,'0.4f')
# print(formatted)
# # second 
# print("1 BRL = {rate:0.2f} USD".format(rate = brl))
# above formatting specifier is '0.2f'.The rate part in the replacement field is not part of the formatting specifier. it determines which keyword argument of .format() goes into that field

# third
# print(f'1 USD = {1 / brl:0.2f} BRL')
# # again, the Specifier is '0.2f'.the 1 / brl expression is not part of it
# # ----------------------------------- formatting specification mini language --------------------------------------

# print("Hello {}".format('pranjal','>'))

# # old style string formatting (% formatter)
# print('Hello Mr. %s'%'Bob')
# # %x formatter to convert int value to hexadecimal value
# errnor = 536382929
# print('Error is %x'%errnor)

class ID:
    # attributes
    def __init__(self,name:str,ssn:str):
        self.name = name
        self.SSN = ssn

    @classmethod
    def getPersistentCard(cls):
        return cls('Pranjal','3ZG12H22')
    
    def __str__(self) -> str:
        return f"CARD:\nName:{self.name},\nSSN:{self.SSN}"
    
    def __repr__(self) -> str:
        return f"CARD:\nName:{self.name},\nSSN:{self.SSN}"

# str.format()
names = {"name":'Pranjal',"weight":93.2,"height":'6.2ft'}

citizen = {"SSN":33422,"Gender":'MALE','AGE':20}

"""
Format string Contain "replacement fields" surrounded by curly braces {}. Anything that not contained inside the braces are considerd as literal text, which is copied unchanged to the output
replacement field = "{" [field_name] ["!" conversion] [":" format_spec] "}".

in less formal terms, the replacement field can start with field_name that specifies the object whose value is to be formatted and inserted into the output instead of replacement field.
after :(colon) a format_spec is specified.

Three Conversion flags are currently supported '!s' which calls str(), '!r' calls repr() and '!a' calls ascii()
The Conversion field causes type coercion (generally it is typecasting by passing a variable of other type to the function whose nams is identical to the desired type) before formmating.

format_spec field contains a specification of how the value should be presented,
including such as field width,alignment,padding,decimal precesion and so on.

A format_spec field can also include nested replacement fields within it. These nested replacement fields may contain a field name, conversion flag and format specification, but deeper nesting is not allowed. The replacement fields within the format_spec are substituted before the format_spec string is interpreted. This allows the formatting of a value to be dynamically specified.

--------------- general form of standard format specifier          ---------------------------------------------

format_spec     ::=  [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

-----------------------------------------------------------------------------------------------
Option

Meaning

'<'

Forces the field to be left-aligned within the available space (this is the default for most objects).

'>'

Forces the field to be right-aligned within the available space (this is the default for numbers).

'='

Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types. It becomes the default for numbers when ‘0’ immediately precedes the field width.

'^'

Forces the field to be centered within the available space.
"""
# print(ID.getPersistentCard())
# id = ID('Harnoor','G11HTRUSA33')
# print("Printing ID{:e} Agustus".format(8334.423))


# A hashable Vector 2D..........................
#  To make our Vector2D hashable or immutable we need to implement __hash__ (__eq__ is also required).
# We need to make our vector instances immutable
class Vector2DHashable:
    __match_args__ = ('x','y')
    typecode = 'd'
    def __init__(self,x,y):
        self._x_var = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x,self.y))
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)
    
    def __str__(self) -> str:
        return "Called __str__ "+str(tuple(self))
    

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array.array(self.typecode,self)))
    
    def __eq__(self, __value: object) -> bool:
        return tuple(self) == tuple(__value)
    
    def __abs__(self):
        return math.hypot(self.x,self.y)
    
    # making it hashable
    def __hash__(self) -> int:
        return hash((self.x,self.y))
    
    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        print(typecode)
        memv = memoryview(octets[1:]).cast(typecode) # to access the internal data of an object
        # changing the value
        return cls(*memv)
    
_=2
v1 = Vector2DHashable(_,0)
v2 = Vector2DHashable(3.2,5.6)

# print(hash(v1),hash(v2))
# st = {v1,v2}

# Supporting Positional Pattern Matching ........................................................

def keyword_pattern_matching(v:Vector2DHashable) -> None:
    match v:
        case Vector2DHashable(x = 0,y = 0):
            print(f'{v!r} is null')

        case Vector2DHashable(x = 0):
            print(f'{v!r} is vertical')

        case Vector2DHashable(y = 0):
            print(f'{v!r} is horizontal')
        
        case Vector2DHashable(x = x,y = y) if x == y:
            print(f'{v!r} is diagonal')

        case _:
            print(f'{v!r} is awesome')


def positional_pattern(v:Vector2DHashable):
    match v:
        case Vector2DHashable(_,0):
            print(f'{v!r} is horizontal')


# positional_pattern(v1)  Before: this will throw an error (TypeError) Vector2DHashable accepts 0 positional sub-patterns
#  to make this work with positional patterns we need to add a class attribute named __match_args__, listing the instance attributes in the order they will be used for postional pattern matching.
            
positional_pattern(v1)

