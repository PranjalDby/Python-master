# in this problem we have to find the sum of the contigous subarray of numbers which has the largest sum

def maximum_crossing_subarray(a,low,mid,high):
    left_sum = -1 * float('inf')
    sums = 0
    max_left = -1
    max_right = -1
    # maximum subarray sum in left-half
    for i in range(mid,low,-1):
        sums = sums + a[i]
        if sums >  left_sum:
            left_sum = sums
            max_left = i
    
    # maximum subarray sum in right-half
    right_sum = -1 * float('inf')
    sums = 0
    for j in range(mid+1,high):
        sums += a[j]
        if sums > right_sum:
            right_sum = sums
            max_right = j

    
    return (max_left,max_right,left_sum + right_sum)




def maximum_subarray(a,low,high)->tuple[int]:
    # Base Case

    if low == high:
        return (low,high,a[low])

    else:
        # This part divides the array into two halves
        mid = (low + high)//2

        # called for left halve
        (left_low,left_high,left_sum) = maximum_subarray(a,low,mid)
        # called for right halve
        (right_low,right_high,right_sum) =maximum_subarray(a,mid+1,high)

        # Maximum subarray sum such that the subarray crosses the midpoint
        (cross_low,cross_high,cross_sum) = maximum_crossing_subarray(a,low,mid,high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return(right_low,right_high,right_sum)

        else:
            return (cross_low,cross_high,cross_sum)

prices =[100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]

difference = [0] * (len(prices))

for i in range(len(prices) ):
    difference[i] = prices[i+1]-prices[i]


print(maximum_subarray(difference,1,len(difference)-1))

print('Testing GPG')