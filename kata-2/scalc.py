#!/usr/bin/python -tt

# String Calculator - Interactions
# http://osherove.com/tdd-kata-2/

import sys

from Calculator import Calculator

def get_input(text):
	print(text, end="")
	return input()

def calc_and_print(numbers):
	print("The result is ", end="")
	calcer = Calculator()
	total = calcer.add(numbers)

def main(*files):
	calc_and_print(files[0])
	while True:
		numbers = get_input("another input please: ")
		if numbers == "":
			break

		calc_and_print(numbers)



if __name__ == "__main__":
    try:
        main(*sys.argv[1:])
    except IOError:
        handle_error()