#!/usr/bin/env python3
from collections import Counter
# demo sliding window algorithm:find the minimum window in s to contain all the chars in t

def solution(s, t):
    # put string t in a counter
    t_counter = Counter(t)
    # test purpose
    print(t_counter)
    
    n = len(s)
    begin = 0
    end = 0
    sub_ls = []
    for begin in range(n):
        if s[begin] not in t_counter.keys():
            continue
        else:
            t_counter_cy = t_counter.copy()
            for end in range(begin,n):

                if s[end] in t_counter_cy.keys():
                    if t_counter_cy[s[end]] > 0:
                        t_counter_cy[s[end]] -= 1
                    if sum(t_counter_cy.values()) == 0:
                        sub_ls.append(s[begin:end+1])
                        break

    # sub_ls is the list with results
    min_str = sub_ls[0]
    for i in range(1,len(sub_ls)):
        if len(min_str) > len(sub_ls[i]):
            min_str = sub_ls[i]
        
    return min_str






s = "ADOBECODEBANC"
t = "ABC"

print(solution(s, t))
 
