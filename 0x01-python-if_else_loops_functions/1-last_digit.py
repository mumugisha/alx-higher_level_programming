#!/usr/bin/python3
import random

def get_last_digit(number):
    return abs(number) % 10

def main():
    number = random.randint(-10000, 10000)
    last_digit_number = get_last_digit(number)

    if last_digit_number > 5:
        print(f"Last digit of {number} is {last_digit_number} and is greater than 5")
    elif last_digit_number < 6 and last_digit_number != 0:
        print(f"Last digit of {number} is {last_digit_number} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is 0 and is 0")

if __name__ == "__main__":
    main()
