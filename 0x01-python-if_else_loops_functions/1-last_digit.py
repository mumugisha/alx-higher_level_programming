#!/usr/bin/python3
import random

 number = random.randint(-10000, 10000)
 last_digit_number = abs(number) % 10

    if last_digit_number < 0
        last_digit_number = -last_digit_number
        print(f"Last digit of {number:d} is {last_digit_number:d} and is ", end="")
    if last_digit_number > 5:
        print(f"Last digit of {number} is {last_digit_number} and is greater than 5")
    elif last_digit_number < 6 and last_digit_number != 0:
        print(f"Last digit of {number} is {last_digit_number} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is 0 and is 0")
