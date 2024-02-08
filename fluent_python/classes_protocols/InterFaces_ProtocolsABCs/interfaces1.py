# Two Kinds of Protocols

#Example 13-1: Partial sequence protocol implementation with __getitem__

from typing import Sequence


class Vowels:

    def __getitem__(self,i):
        return 'AEIOU'[i]
    

v = Vowels()
print(v[:-1])

print('E' in v)

Sequence