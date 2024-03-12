#!/usr/bin/python3
for y in range (0, 10):
    for z in range(y+1, 10):
        if y == 9 and z == 5:
            print('95')
        else:
            print('{}{}, '.format(y, z), end= '')
