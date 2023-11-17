# the identity of character-- its code point -- is a number from 0 to 1,114,111
"""
base 10
- with U+ prefix

decoding:- converting from bytes to code point is called decoding.

encoding:- converting from code point to bytes is called encoding
"""
s = "cafè"
print(len(s))
# s contains 4 unicode chars
# encode
import timeit
start = timeit.default_timer()
passs = str(input('Enter The Password: '))
b = passs.encode('utf_16')
end = timeit.default_timer()
print('Time Taken is = {}'.format(end-start))
print(b)

# decoding
print(b.decode(encoding='utf-16'))

# bytes and bytearray
# bytes are immutable array of bytes
cafe = bytes('cafë',encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])

# bytearray
cafe_arr = bytearray(cafe)
print(cafe_arr)
# basic encoders and decoders

for codec in ['latin_1','utf_8','utf_16']:
    print(codec,'El Niño'.encode(codec),sep='\t')