#!/usr/bin/env python3

# in an array having n integers, find the maximum sum of k consecutive integers in the list
def solution(ls, k):
    n = len(ls)
    max_sum = 0
    for i in range(n-k+1):
        print(i)
        if sum(ls[i:i+k]) > max_sum:
            max_sum = sum(ls[i:i+k])
    return max_sum

ls = [4, 5, 9, 3, 2, 8, 12]
k = 3

print(solution(ls, k))

