#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit_number = abs(number) % 10

if number < 0:
    last_digit_number = -last_digit_number

if last_digit_number > 5:
    print(f"The last digit of {number} is {last_digit_number} and is greater than 5\n")
elif last_digit_number < 6 and last_digit_number != 0:
    print(f"The last digit of {number} is {last_digit_number} and is less than 6 and not 0\n")
else:
    print(f"The last digit of {number} is {last_digit_number} and is 0\n")
