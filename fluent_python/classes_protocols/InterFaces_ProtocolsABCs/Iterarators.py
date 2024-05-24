# Creating Iterarators that
# Yeilding the original data

class SequenceIterator:
    def __init__(self,sequence) -> None:
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            item  = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        

# itrator = SequenceIterator(['Pranjal','Emily','Juli','Mayuko'])

# for items in itrator:
#     print(items)


# How for loop works internally

# itr = iter(itrator)

# while True:
#     try:
#         # retrieve the next item
#         item = next(itr)

#     except StopIteration:
#         break

#     else:
#         #the loop code block goes here
    
#         print(item)


# 2. Ṭransforming the input data
        
class ModifiedSequenceIterator:
    def __init__(self,sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            squre = self._sequence[self._index] ** 2
            self._index += 1
            return squre
        
        else:
            raise StopIteration
        
# mdfiedSqItr = ModifiedSequenceIterator([2,4,6,8,10,20])
# for item in mdfiedSqItr:
#     print(item)

# Generating the new Data :: We can also create a custom iterators that generate a stream of new data from a given computation without taking a datat stream as input.

class FibonnaciIterator:
    def __init__(self,stop = 10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index <= self._stop:
            self._index += 1
            fib_number = self._current
            self._current,self._next = self._next,self._current + self._next

            return fib_number
        else:
            raise StopIteration
        

# fibnn = FibonnaciIterator(1000)
# for i in fibnn:
#     print(i,end=",")

# print("")

# creating potentially infinite Iterator

# class InfiniteFibonacciGenerator:
#     def __init__(self):
#         self._index = 0
#         self._current = 0
#         self._next = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self._index += 1
#         self._current,self._next = self._next,self._current + self._next
#         return self._current
    


# for infinity in InfiniteFibonacciGenerator():
#     print(infinity,end=",")

# Inheriting from collections.abc.Iterator

from collections.abc import Iterator
class SequenceIterator2(Iterator):
    def __init__(self,sequence):
        self._sequence = sequence
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index +=1
            return item
        else:
            raise StopIteration
        

seq = ['AlanWalker','Emma Stone','Gennie']

# st = SequenceIterator2(seq)
# for s in st:
#     print(s)

# -------------------------------- creating Generator Functions -------------------------------------------- 

def sequence_generator(sequence):
    
    for item in sequence:
        yield item # this is our generator functions definition

    """Above Statement return one item at a time"""
sq_generator = sequence_generator(['Alan Walker','Pranjal Dubey','Emilly','Elly','Emma'])

print(next(sq_generator)) # it is type of generator object

# but if we traverse it through we see that it act as like an Iterator
print('after printing first item the index is incremented to the next item')
for i in sq_generator:
    print(i)

# ----- Using generator expression to Create Iterators
# We can create genexp using ()
genexp = (item for item in [2,4,8,12,43,21])
print(genexp) # this returns the generator object