#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sand = 0
    for a in range(x):
        try:
            print(my_list[a], end="")
            sand += 1
        except IndexError:
            break
    print("")
    return sand
