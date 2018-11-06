#!/usr/bin/env python3

def solution(ls, k):
    # return the maximun sum of k consecutive elements in list ls 
    n = len(ls)   
    max_sum = 0
    sub_sum = 0
    # calculate the sum of the first k elements
    for i in range(k):
        sub_sum += ls[i]
    max_sum = max(max_sum, sub_sum)
    
    # calculate the sum of k consecutive elements in ls by deque
    for i in range(1,n-k+1):
        sub_sum = sub_sum - ls[i-1] + ls[i+k-1]
        max_sum = max(max_sum, sub_sum)
    return max_sum

ls = [4, 5, 9, 3, 2, 8, 12]
k = 3

print(solution(ls, k))

 
