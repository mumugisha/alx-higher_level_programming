#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for i in range(len(roman_string)):
        if i > 0 and digits[roman_string[i]] > digits[roman_string[i - 1]]:
            total += digits[roman_string[i]] - 2 * digits[roman_string[i - 1]]
        else:
            total += digits[roman_string[i]]

            return total
