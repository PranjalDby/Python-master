# Although there is a generic UnicodeError exception, the error reported by python is usually more specific:
# either UnicodeEncode error (When converting str to binary sequences)
# UnicodeDecode Error (while converting from binary sequences to str)

# coping with UnicodeEncodeError

#  Most non-UTF codecs handle only a small subset of the Unicode characters. When
#  converting text to bytes, if a character is not defined in the target encoding, Unico
#  deEncodeError will be raised

s = 'Sao Paulo'

print(s.encode('utf-16'))

# handling EncodeError
print(s.encode('cp437',errors='ignore'))
# ignore
# replace
print(s.encode('cp437',errors='replace'))
# xmlcharrefreplace
print(s.encode('cp437','xmlcharrefreplace'))