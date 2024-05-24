# A tuple built from another is actually the same tuple

t1 = (1, 2, 3)
t2 = tuple(t1)
t3 = t1[:]
print(t2 is t1)  # True
print(t3 is t1)  # True

# Example 6-18: String literal may create shared objects

t1 = (1, 2, 3)
t3 = (1, 2, 3)

print(t3 is t1)  # False

s1 = 'ABC'
s2 = 'ABC'

print(s2 is s1)  # True

# The Sharing of string literals is an optimization technique called interning.Cpython uses it to store only one copy of each distinct string value.
# Interning also works for small integers like -1,1,0 etc.