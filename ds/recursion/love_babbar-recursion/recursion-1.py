import timeit
def gotoHome(src:int,des:int,start_time:float):
    if src == des: # base-case
        stop = timeit.default_timer()-start_time
        print('Reached Home at {:e}s'.format(stop))
        return
    
    src = src + 1 #processing
    gotoHome(src,des,start_time) #Recursive relation

# third number is equal to sum of first two number
def fibonnaci(n,memo):
    if n <= 1: #base case
        return n
    
    memo[n] = fibonnaci(n-1,memo) + fibonnaci(n-2,memo)

    return memo[n] #processing

# countDistinct - Way to climb stair
ans = [0,1]
# under-progress DP
def countDistinctWay(n):
    if n < 0:
        return 0

    if n == 0:
        return 1
    
    for i in range(2,n+1):
        res = countDistinctWay(n-1) + countDistinctWay(n-2)
        ans.append(res)
    
    return ans[n]


mapping_digits = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
array = []
def sayDigit(digits,remainder):
    if digits < 10:
        array.append(mapping_digits[digits])
        return
    
    quotient,remainder = divmod(digits,10)
    array.append(mapping_digits[remainder])
    sayDigit(quotient,remainder)

if __name__ == "__main__":
    start = timeit.default_timer()
    # fibonnaci series using for-loop
    # t1 = 0
    # t2 = 1
    # sums = t1 + t2
    # for i in range(1,n+1):
    #     t1 = t2
    #     print(t1,end=" ")
    #     t2 = sums
    #     sums = t1 + t2

    digits = 6392057090
    # print(divmod(412,10))
    sayDigit(digits,1)
    print(array[::-1])


