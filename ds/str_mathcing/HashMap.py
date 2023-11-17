
class Node[T_key,T_val]:
    def __init__(self, key:T_key, val:T_val):
        self.key = key
        self.val = val
        self.next = None
        self.hashcode:int = -1

BLANK = object()
class HashMap[T_key,T_val]:
    def __init__(self, size:int):
        self.size = size
        self.table = [BLANK] * size

    def __len__(self):
        return self.size
    
    def hash_function(self, key:T_key):
        return sum(
            ord(x) for x in repr(key).lstrip("'")
        ) % self.size 
    
    def __setitem__(self,key:T_key,value:T_val):
        index = self.hash_function(key)
        print(index)
        self.table[index] = value

    def __getitem__(self,key:T_key):
        val = self.table[self.hash_function(key)]

        if val == BLANK:
            raise KeyError
        
        return val
    
    def __delitem__(self,key:T_key):
        print('delitem called')
        index = self.hash_function(key)
        print(self[index])
        self[index] = BLANK

def hash_function(key):
    hashed = 0
    for i in range(len(key)):
        hashed += ord(str(key[i]))

    return hashed % len(key)


hashtable = HashMap(size=100)
hashtable[1]='a'
hashtable[2]='pranjal'
hashtable[3]='aryan'
hashtable[4]='sumit'
hashtable[5]='Joseph'
hashtable['ariana'] = 'Grande'
hashtable[10] = 'Markus'
# del hashtable[2]
hashtable[3] = 'Taylor Swift'
print(hashtable[3])

passw = str(input('Enter password: '))

hashed = hash_function(passw)
print(hashed)
print('Hashed Password = ',passw == hashed)