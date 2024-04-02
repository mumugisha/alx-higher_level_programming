#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0): 
    sand = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            sand += 1
        except (ValueError, TypeError):
            pass
    print()
    return sand
