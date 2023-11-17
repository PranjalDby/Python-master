
def get_prime(num):
    if num != 1 or num != 0:
        for i in range(num,(num * 4) // 2):
            if num % i != 0:
                return i
            
    return len(num)

d = 256
def get_hash(pattern,l):
    h = 0
    for i in range(l):
        h += (d ** i + ord(pattern[i])) 
        # print(h)
    return  h

w = 4
def search_patter(text,search):
    x = len(search)
    t = len(text)
    hash_pattern = 0
    text_window = 0
    h = 1
    for i in range(x-1):
        h = (h * d) % q

    for i in range(x):

        hash_pattern = ((d * hash_pattern) * ord(search[i])) % q
        text_window = ((d * text_window) * ord(text[i])) % q
    
    i = 0
    j = 0
    for i in range(t-x+1):
        if hash_pattern == text_window:
            print(f'true when i = {i}')
            for j in range(x):
                if text[i+j] != search[j]:
                    break
                else:
                    j+=1

            if j == x:
                print('Pattern Found at position  {}'.format(i))

        # calculating hash value of next window of text
        if i < t-x:
            hash_pattern = (d * (t-ord(text[i]) * h) + ord(text[i+x])) % q
            if t < 0:
                t = t + q

txt = "pranjal dubey roll no 11"
pat = "bey"

print(txt.strip(' ').replace(' ',''))
txt = txt.replace(' ','')
print(txt)
q = get_prime(len(txt))

search_patter(txt,pat)