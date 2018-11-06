#!/usr/bin/env python3
from collections import Counter


def check_dup(s):
    """Check if the string contains all unique characters; if yes,return true, otherwise false"""
    dup = Counter(s)
    for key in dup.keys():
        if dup[key] > 1:
            return False
    return True

def solution(s):
    """Find the longest substring without repeating characters"""
    n = len(s)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        ls = []
        for i in range(n):
            for j in range(i+1, n):
                if check_dup(s[i:j]):
                    print(i)
                    print(j)
                    ls.append(len(s[i:j]))
        return max(ls)                     

s = ' '
print(check_dup(s))
print(solution(s))
    
   
