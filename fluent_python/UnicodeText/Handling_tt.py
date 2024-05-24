# Normalizing Unicode for Reliable Comparisons
from unicodedata import normalize,name
import unicodedata
# Some Normalization forms
# NFC - keyboard intruptted chars
# NFKC - k stands for compatibilty
# NFKD
s1 = 'cafè'

s2 = 'cafe\N{COMBINING ACUTE ACCENT}'

print(s1,s2)

print(len(normalize('NFC',s1)))

half = '\N{VULGAR FRACTION ONE HALF}'

print(normalize('NFKC',half))

# NOTE : NFKC AND NFKD CAUSES DATA LOSS AND SHOULD BE APPLIED ONLY FOR SEARCHING AND INDEXING

# NOTE : case folding is another useful operation for searching and another operation

# case folding is essentially converting all text to lower case, with some additional transformation
micro  = 'µ'

print(name(micro))
micro = micro.casefold()
print(name(micro))

# extreme normalization

def shave_marks(txt):
    # remove all diacratics from marks"
    norm_txt = normalize('NFD',txt)
    shaved = "".join(c for c in norm_txt if not unicodedata.combining(c))

    return unicodedata.normalize('NFC',shaved)

order  =  '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'

print(shave_marks(order))