# Subclassing an ABC

# Example: 13-6. frenchdeck2.py: FrenchDeck2,a subclass of collections.MutableSequence

from collections import namedtuple,abc
from operator import indexOf
import re
from turtle import position

Card = namedtuple('Cards',['rank','suit'])

class FrenchDeck2(abc.MutableSequence):
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spade,diaomonds,club,heart'.split(',')

    def __init__(self) -> None:
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    
    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
    
    def __setitem__(self,position,value): #1
        self._cards[position] = value

    def __delitem__(self,position): #2
        del self._cards[position]

    
    def insert(self,position,value): #3
        self._cards.insert(position,value)


# Meanings of Points Listed Above

"""
#1: __setitem__ is all we need to enable shuffling
#2: ... but subclassing MutableSequence forces us to implement __delitem__, an abstract method of an ABC
#3:  we are also required to implement insert, the third abstract method of MutableSequence
# If we not implement any of the required abstract method we get an error: Can't instantiate "class name" with abstract method "method name", this is an a type error
"""

# fdeck = FrenchDeck2()

# print(fdeck[0])

#  -----------------------------------------------------------------------------------------------------------------------

import bisect
import sys

# def sortHelper(items,low,high):
#     if low >= high:
#         return
#     else:
#         mid = low + (high-low) // 2
#         # left-subpart
#         sortHelper(items,low,mid)
#         # righ-subpart
#         sortHelper(items,mid+1,high)
#         merge(items,low,mid,high)

# def merge(items,low,mid,high):
#     temp_mergingArray = [0] * (high-low + 1)
#     x = low
#     y = mid + 1
#     z = 0
#     while(x <= mid and y <= high):
#         if items[x] < items[y]:
#             temp_mergingArray[z] = items[x]
#             z+=1
#             x+=1
#         else:
#             temp_mergingArray[z] = items[y]
#             y+=1
#             z+=1
    
#     # for remaing parts
#     while( x <= mid):
#         temp_mergingArray[z] = items[x]
#         z+=1
#         x+=1
    
#     while (y <= high):
#         temp_mergingArray[z] = items[y]
#         z+=1
#         y+=1

#     for i in range(low ,high + 1):
#         items[i] = temp_mergingArray[i-low]


# def checkNeedleIsAvailable(sortedHaystack,needle):

#     mid = (len(sortedHaystack)-0)//2

#     if needle < sortedHaystack[mid]:
#         for i in range(0,mid):
#             if sortedHaystack[i] == needle:
#                 return i
    
#     else:
#         for j in range(mid,len(sortedHaystack)):
#             if sortedHaystack[j] == needle:
#                 return j
            
#     return -1
        
    
# def getNeedleIndex(haystack,needle):

#     if len(needle) == 0:
#         return 0
#     hay = [-1 for i in range(len(haystack))]
#     # converted a string into a list of ascii values
#     for i in range(len(haystack)):
#         hay[i] = ord(haystack[i])

#     # converting our needle into a list of ascii values
#     __needle = [-1] * (len(needle))

#     for j in range(len(needle)):
#         __needle[j] = ord(needle[j])

#     # sorting our haystack
    
#     sortHelper(hay,0,len(hay)-1)
#     print(hay)

#     # sorting needle
#     sortHelper(__needle,0,len(__needle)-1)
#     print(__needle)
#     index = []
#     res = -1
#     for i in range(len(__needle)):

#         indx = checkNeedleIsAvailable(hay,__needle[i])
#         if indx not in index and indx != -1:
#             index.append(indx)

#         else:
#             break
    
#     print(len(index))
#     if index != []:
#         ss = ""
#         for i in index:
#             ss += str(i)
        
#         res = int(ss)
    
#     return res

# Bisect Implementation

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]

NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

row_fmt = '{0:2d} @ {1:2d}     {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK,needle) #1
        offset = position * '  |' #2
        print(row_fmt.format(needle,position,offset))#3


breakpoints = [60,70,80,90]
grades = 'FDCBA'

def getGrade(score):
    i = bisect.bisect(breakpoints,score)
    print(f'i = {i} for score = {score}')
    return grades[i]

if __name__ == "__main__":
    

    # if sys.argv[-1] == 'left': #4
    #     bisect_fn = bisect.bisect_left
    
    # else:
    #     bisect_fn = bisect.bisect

    # print('DEMO:',bisect_fn.__name__) #5
    # print('haystack ->', ' '.join(f'{n:2}' for n in HAYSTACK))
    # demo(bisect_fn)


    # Meaning of Above points
    """
    #1:Use the choosen bisect function to get the insertion point.
    #2:Build a pattern of vertical bars proportional to the offest.
    #3:Print formatted row showing needle and insertion point.
    #4:Choose the bisect function to use according to the last command-line argument.
    #5:Print header with name of function selected 
    """

    res = [getGrade(score) for score in [55,60,65,70,75,80,85,90,95]]
    print(res)

    rs = [55,60,65,70,75,80,85,90,95]

    # i = bisect.bisect(breakpoints,65)
    # print(i)
    # bisect.insort(rs,56)
    # print(rs)
