#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit_number = number % -10
else:
    last_digit_number = number % 10
if last_digit_number > 5:
    print("Last digit number of {:d} is {:d} and is greater than 5"
          .format(number, last_digit_number))
elif last_digit_number < 6 and last_digit_number != 0:
    print("Last digit number of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit_number))
else:
    print("Last digit number of {:d} is 0 and is 0".format(number))
