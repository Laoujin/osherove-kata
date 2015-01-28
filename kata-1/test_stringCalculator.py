#!/usr/bin/python -tt

# String Calculator
# http://osherove.com/tdd-kata-1/

############################ TEST SUBJECT

def add(numbers):
	if numbers == "":
		return 0

	return int(numbers)

################################### TESTS

def test_empty_string_returns_0():
	assert add("") == 0

def test_single_number_converts_to_number():
	assert add("1") == 1
	assert add("5") == 5
