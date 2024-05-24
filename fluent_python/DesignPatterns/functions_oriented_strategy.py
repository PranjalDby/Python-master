from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional,Callable,NamedTuple

class Customer(NamedTuple):
    name:str
    fidelity:int

class LineItem(NamedTuple):
    product:str
    quantity:int
    price:Decimal

    def total(self):
        return self.price * self.quantity

class Order(NamedTuple):# This is Context of our strategy DP
    customer:Customer
    cart:Sequence[LineItem]
    promotion:Optional[Callable[['Order'],Decimal]] = None # it is an optional callable class method

    def total(self) -> Decimal:
        total = (item.total() for item in self.cart)
        return sum(total,start=Decimal(0))
    
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self) # Calls an Callable which get Invoked by passing an instance of Order
            return self.total() - discount
        
    def __repr__(self) -> str:
        return f'<Order total : {self.total():.2f} due : {self.due():.2f}'
    
# Implementing strategy using first class objects
def fidelity_promo(order: Order) -> Decimal:
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal(0.05)
    
    return Decimal(0)

def bulk_item_promo(order:Order):
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal(0.1)
    
    return discount


# Finding Startegies in a Module
"""
Moudles in python are also a first class objects, and the standard library provides serveral functions to handle them.
example: -  the built in globals()

globals() : return dictionary containing current global system table. this is always the dictionary of the current module (inside a functions or method,this is the module where it is defined, not the the module from which it is called)
"""

# Example 10-7: the promos list os built by introspection of the  module global namespasce
#  the bulk_item_promo,fidelity_promo was already in our global name space

promos = [promo for name,promo in globals().items()
          if name.endswith('_promo') and name != 'best_promo'] #here we filter out best_promo method to avoid any infinite recursion


def best_promo(order:Order)->Decimal:
    return max(promo(order) for promo in promos)
# -------------------------------------------- Decorator Enhanced Strategy pattern------------------------

Promotion = Callable[[Order],Decimal] # Register Decorator
promos:list[Promotion] = []

def promotion(promo:Promotion) -> Promotion: # Decorator
    promos.append(promo)
    return promo

@promotion
def fidelity_decorated(order:Order) -> Decimal:
    """ 5 % discount """
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal(0.05)
    
    return Decimal('0')

@promotion
def bulkItemPromo_decor(order:Order):
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal(0.1)
    
    return discount


"""
1. Above promotion is a registration decorator: it returns the promo function unchanged, after appending it to the promo list.
2. Any functions decorated by @promotion will be added to prmos.

The above solution has several advantages:
    • The promotion strategy functions don't have to use special names—no need for
    the _promo suffix.
    • The @promotion decorator highlights the purpose of the decorated function, and
    also makes it easy to temporarily disable a promotion: just comment out the
    decorator.
    • Promotional discount strategies may be defined in other modules, anywhere in
    the system, as long as the @promotion decorator is applied to them.
"""
john = Customer("John",5600)
Anjelina = Customer("Anjelina",65000)

cart = [LineItem("toiletPapers",30,Decimal(2.45)),
        LineItem("Banana",20,Decimal(1.22)),
        LineItem("Orange",10,Decimal(2.12))]

john_order = Order(john,cart,bulkItemPromo_decor)
print(best_promo(john_order))