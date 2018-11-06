#!/usr/bin/env python3

# dynamic programming
def max_subarray(ls):
    # ls is not empty list
    max_i = max_sub = ls[0]
    for i in ls[1:]:
        max_i = max(i, max_i + i)
        max_sub = max(max_i, max_sub)
    return max_sub

ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(ls))

# recursive in a way as below is not working
def max_sub(ls):
    if len(ls) > 1:
        return max(max_sub(ls[:-1]), max_sub(ls[:-1])+ls[-1])
    if len(ls) == 1:
        return ls[0]

#ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#print(max_sub(ls))

