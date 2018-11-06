#!/usr/bin/env python3

# Pick out the single number that doesn't have duplicate number in the list
# Way to go is to create another list, add if the number is not in the new list, delete if already in the new list

def single_number(ls):
    
    new_list = []
    
    for i in ls:
        if i in new_list:
            new_list.remove(i)
        else:
            new_list.append(i)

    return new_list

ls = [2, 2, 4, 4, 9]

#print(single_number(ls))
 
# Using dictionary as hash table

def h_table(ls):
    
    new_dict = {}
    for i in ls:
        try:
            new_dict.pop(i)
        except:
            new_dict[i] = 1
    return new_dict.popitem()[0]

print(h_table(ls))   
