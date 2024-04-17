#!/usr/bin/python3

"""Reads from standard input and computes metrics.
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys

def print_stats(size, status_codes):
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                code = parts[-2]
                if code in valid_codes:
                    size += int(parts[-1])
                    status_codes[code] = status_codes.get(code, 0) + 1
            except (IndexError, ValueError):
                pass

            count += 1
            if count == 10:
                print_stats(size, status_codes)
                count = 0

        if count != 0:
            print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
