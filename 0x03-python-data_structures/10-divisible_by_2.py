#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    kenya_list = []

    for num in my_list:
        if num % 2 == 0:
            kenya_list.append(True)
        else:
            kenya_list.append(False)

    return kenya_list
