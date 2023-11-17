# for relatively small k = number of integers
def counting_occurances(arr,n):
    occurances = []
    max = get_max(arr,n)

    for i in range(arr[max] + 1):
        occurances.insert(i,0)
    

    for i in range(n):
        if arr[i] not in occurances:
            occurances[arr[i]] += 1
    
    print(occurances)

    # cummlative sum
    for i in range(0,len(occurances)-1):
        sum = occurances[i]
        occurances[i+1] = occurances[i+1] + sum    
    
    print(occurances)
    for j in range(len(occurances)-1,0,-1):
        occurances[j] = occurances[j-1]

    output = [0] * n
    for i in range(len(arr)):
        output[occurances[arr[i]]] = arr[i]
        occurances[arr[i]] += 1
    
    print(output)

def get_max(arr,n)-> int:
    max = 0
    for i in range(1,n):
        if arr[max] < arr[i]:
            max = i

    return max

arr = [3,3,7,6,5,5,5]
# arr = [4,2,2,3,1,8,5,6]
counting_occurances(arr,len(arr))