#!/usr/bin/python3
for letter in range(ord('a'), ord('{')):
     letter = chr(letter)
     if letter not in 'qe':
         value = ord(letter)
         print("{:c}".format(value), end="")
