import sys
from string import printable
from hash_distribution import plot, distribute
def hashing_string(string):
    return sum(
        index * (ord(char))
        for index, char in enumerate(repr(string).lstrip("'"),start=1)
    ) % 101

plot(histogram=distribute(printable,6,hashing_string))

# print(hashing_string('Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum mollitia dolor tempore aliquid recusandae. A officiis error dolore ad perspiciatis porro? Dolorem tenetur qui sapiente, reprehenderit eos molestiae impedit? Quas repellat qui, quidem voluptate delectus deserunt odio ipsam esse laborum, iure consequuntur nulla ex facere.'))
# print(hashing_string(123))
# print(hashing_string('123'))  
# # Same Hashcode Shows that there is a collision and causes a problem of clustering
# print(hashing_string('lorem'))
# print(hashing_string('merol'))

print(hashing_string('a'))
print(hashing_string('b'))
print(hashing_string('c'))
print('hash function currently used by python is: ', sys.hash_info.algorithm)