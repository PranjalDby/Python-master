import unicodedata
import re

re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for ch in sample:
    print(f"U+{ord(ch):04x}", ch.center(6), 're_dig' if re_digit.match(ch) else '-', 'isdig' if ch.isdigit() else '-', 'isnum' if ch.isnumeric() else '-', format(unicodedata.numeric(ch), '5.2f'), unicodedata.name(ch), sep='\t')



# Completed .........
