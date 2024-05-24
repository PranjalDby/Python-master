class Coordinates:

    def __init__(self,x,y):
        #private attributes
        self._x = x
        self._y = y

    # getter and setter approach

    #accessor
    def get_x(self):
        return self._x

    #mutator
    def set_x(self,val):
        self._x = val


    #accessor
    def get_y(self):
        return self._y

    #mutator
    def set_y(self,val):
        self._y = val



pnt = Coordinates(12,5)

print(pnt.get_x())
print(pnt.get_y())

# using python property -------------------------------------

# creating attributes using properties


class CircleCLass:
    def __init__(self,radius):
        self._radius = radius

    def _get_radius_(self):
        print("Get radius")
        return self._radius
    
    def _set_radius(self,radi):
        print("Set radius")
        self._radius = radi 
    

    def _del_radius(self):
        print("del radius")
        del self._radius

    # #using lambda function as getter defining property
    # radius = property(lambda self:self._radius)

    
    radius = property(
        fget=_get_radius_,
        fset=_set_radius,
        fdel=_del_radius,
        doc="Radius Property"
    )

circle_larg = CircleCLass(23.4)

"""print(circle_larg.radius) #calling fget
circle_larg.radius = 32.2#calling fset
print(circle_larg.radius.__doc__) #calling fget
print(circle_larg.radius) #calling fget

print(circle_larg.radius.__doc__)
print("edited USing Vim")"""

print(CircleCLass.radius.fset)


# simple example of decorator

def decorator(func,a,b):
    # decorator function
    def decorate_func(*args):
        result_ = func(args[0],args[1])
        fmt_str = f"result of {func.__name__} is {result_}"

        return fmt_str
    
    return decorate_func(a,b)

def sum(a,b):
    return a+b

dec = decorator(sum,20,30)
print(dec)
        
