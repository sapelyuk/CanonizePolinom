#! Sorting keys from dictionary with polynom terms

import math

def get_sorted_keys(dictionary):
    
    keys_list = dictionary.keys()  #getting all keys from dict
    keys_list = list(keys_list)   #making list of keys for sorting

    sorted_keys_list = sorted(keys_list, key = sorting_function)
    sorted_keys_list.reverse()

    return sorted_keys_list

#Sorting function
def sorting_function(imput_key):
    weight = 0
    num = 1

    if imput_key == "free_digit":
        return weight
    
    for char in imput_key:
        if char == "^":
            num = 10
        elif char > "0" and char <= "9":
            weight = weight+pow(num,int(char))
        else:
            weight = weight - ord(char)+122    # making weight of one letter in reverse order in [0;25] 

    return weight