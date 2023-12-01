

def merge_sort(items):
    if len(items) > 1:
        r = len(items) // 2
        L = items[:r] #left subarray
        R = items[r:] #right Subarray

        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                items[k] = L[i]
                i += 1
            
            else:
                items[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            items[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            items[k] = R[j]
            j+=1
            k+=1


def find(duplicate):
    p = 0
    p1 = 1
    dupl = [i for i in range(len(duplicate)+1)]
    for i in range(len(dupl)):
        dupl[i] = 0
    
    while p < p1 and p1 < len(duplicate):
        if duplicate[p1] == duplicate[p]:
            dupl[p] = duplicate[p1]
        
        p1+=1
        p+=1

    print(dupl)


duplicate = [1,2,3,1,4,5,6,2,8,6]
duplte = [3,4,54,6,6,6]
duplicate = duplicate + duplte
print(duplicate)
merge_sort(duplicate)
print(duplicate)
# duplicate.sort(re)
ss = {1:"pranjal"}
for i,v in ss:
    print(i,v)
