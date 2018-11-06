#!/usr/bin/env python3

def median_ls(ls):
    length = len(ls)
    if length == 0:
        return None
    else:
        if length%2 == 0:
            return (ls[length//2-1]+ls[length//2])/2
        else:
            return ls[length//2]


ls = [1, 3, 5, 7]

ls01 = [2, 4, 8]

ls02 = [3, 5, 9, 0]

print(median_ls(ls))
print(median_ls(ls01))
print(median_ls(ls02))


