#!/usr/bin/python -tt

# String Calculator
# http://osherove.com/tdd-kata-1/

############################ TEST SUBJECT

def add(numbers):
	if numbers == "":
		return 0

	if not "," in numbers:
		return int(numbers)

	numbers = numbers.split(",")
	numbers = map(int, numbers)
	return sum(numbers)

################################### TESTS

def test_empty_string_returns_0():
	assert add("") == 0

def test_single_number_converts_to_number():
	assert add("1") == 1
	assert add("5") == 5

def test_two_numbers_get_added():
	assert add("1,2") == 3