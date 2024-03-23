#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    dena = 0

    for topup in my_list:
        number += topup[0] * topup[1]
        dena += topup[1]

    return (number / dena)
