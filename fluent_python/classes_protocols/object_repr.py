# A Vector2D class we see in previous Chapter,embrace with different methods
import array,math
class Vector2D:
    typecode = 'd'
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    

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
    
    # A_c1 
    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        print(typecode)
        memv = memoryview(octets[1:]).cast(typecode)
        # changing the value
        return cls(*memv) 


# An alternative Constructor:
# We have to still create a method that rebuilt our Vector2D from bytes
# Verifying each special methods
v1 = Vector2D(3,4)
x,y = v1 # this call __iter__() method,basically unpacking
print(y)
v1_clone = eval((repr(v1)))
print(v1 == v1_clone) # comparison __eq__
octets = bytes(v1) #here it uses the __bytes__ methods to produce a binary representation
recreated_vector = v1.frombytes(octets)
print(type(recreated_vector))

# memoryview() is applied only to that objects that supports buffer protocol.buit-in objects that support buffer protocol are bytes,bytearray
random_byte_arr = bytearray('ABC','utf-8')
print(random_byte_arr)
memv = memoryview(random_byte_arr)
memv[0] = 68
print(memv.tolist()) 
print(random_byte_arr)

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
    


dm1 = Demo2()
#manual passing the instance of object instance
# dm1.instanceMethod(dm1,'Hello Instance Method')
# calling instanceMethod without creating instance method
# Demo2.instanceMethod() throws error TypeError: Demo2.instanceMethod() missing 1 required positional argument: 'self'
# Demo2().classMethod('MagicShop- Maxce')
# dm1.staticMethod('staticmethod calling')

demo = Demo()
ss = demo.klassMeth('pranjal') # it recieves the classname as the first argument
# proof: (<class '__main__.Demo'>, 'pranjal')
#invoking our staticmethod which is just a old function745
normal_meth = demo.statikmethod('pranjal','johnson')

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
        return cls(['mozzarella','tomatoes'])
    
    @classmethod
    def proscuitto(cls):
        return cls(['mozzarella','tomatoes','ham'])
    
    #staticmethod
    def circle_area(r):
        return math.pi * r**2


#  ------------------------------------ Formated Displays ------------------------------------
"""
the f-string, the format() built-in function, and the str.format() method delegate the actual formmating to each type by calling their .__format__(format_spec) method.
"""
# example:-