#!/usr/bin/env python3


# find the longest substr from the string
def solution(s):
    n = len(s)
    ls = []
    begin = 0
    end = 0
    sub_str_len = 0
    for begin in range(n):
        sub_str = ''
        for end in range(begin,n):
            if s[end] not in sub_str:
                sub_str += s[end]
            else:
                break
        sub_str_len = max(sub_str_len, len(sub_str))
            
    return sub_str_len


s = 'abcabcbb'

print(solution(s))
