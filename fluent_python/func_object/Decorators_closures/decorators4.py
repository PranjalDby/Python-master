# Some More Exercise on generic functions

from decimal import Decimal
from functools import singledispatch

@singledispatch #............... this is our base or generic functions
def func(args,verbose = False):
    if verbose:
        print("Let Me just say, ",end=" ")
    
    print(args)

@func.register(list)
def _2(args,verbose = False):
    if verbose:
        print("Enumerate This: ")

    for i,eleme in enumerate(args):
        print(i,eleme)

@func.register(list)  # with type defined of  first argument
def _1(arg,verbose=False):
    if verbose:
        print("Strength of a Numebr ah...?",end= " ")
    
    print(f"Huh.. True said .. Strength is {sum(arg)}")

# To Enable registering lambda and pre-existing functions, the register() attr can be used in a functional
# form

def nothing(arg,verbose=False):
    print("Nothing.....")

z = lambda x : x * 2.90
func.register(type(None),nothing)
# Applying register() attribute to register lambda
func.register(float,z)


#The register() Attribute returns the undecorated functions. this enables decorator stacking, pickling  

@func.register(float)
@func.register(Decimal)
def fun_num(args,verbose = False):
    if verbose:
        print("half of Your number: ",end= " ")
    
    print(args / 2)

if __name__ == '__main__':
   ss = func(43.33)
   print(ss)
   print(fun_num is func) # False, register() returns an undecorated functions