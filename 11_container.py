#!/usr/bin/env python3

# Leedcode issue 11

def container(ls):
    
    # Make a dictionary hashtable from the list
    ls_dict = dict(enumerate(ls, 1))
    
    print(ls_dict)

    # Find the minimum value in the dict and calculate the biggest area with that element
    # which is with the furthest item
    
    ls_dict_rvs = {value: key for key, value in ls_dict.items()}
    ls_dict_sort = OrderedDict(sorted(ls_dict_rvs.items, key = lambda t: t[0]))
    
    result = []
    for k, v in ls_dict_sort:
        
    
    
        
