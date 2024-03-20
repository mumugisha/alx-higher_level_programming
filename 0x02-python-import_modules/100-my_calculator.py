#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    """Handle basic arthm operations."""

if len(sys.argv) - 1 != 3:
        print("Usage:./100-my calculator.py <a> <operator> <b>")
        sys.exit(1)

        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(ops.key()):
            print("Unknown operator. Available operators: +,-.* and /")
            syst.exit(1)

            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
