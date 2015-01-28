#!/usr/bin/python -tt

# String Calculator
# http://osherove.com/tdd-kata-1/

############################ TEST SUBJECT

def add(numbers):
	if numbers == "":
		return 0

	return 1

################################### TESTS

def test_empty_string_returns_0():
	assert add("") == 0

def test_1_returns_1():
	assert add("1") == 1