#!/usr/bin/python -tt

# String Calculator - Interactions
# http://osherove.com/tdd-kata-2/

import sys

from Calculator import Calculator

def main(*files):
	print("The result is ", end="")

	calcer = Calculator()
	total = calcer.add(files[0])

if __name__ == "__main__":
    try:
        main(*sys.argv[1:])
    except IOError:
        handle_error()