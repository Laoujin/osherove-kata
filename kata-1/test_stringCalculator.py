#!/usr/bin/python -tt

# String Calculator
# http://osherove.com/tdd-kata-1/

############################ TEST SUBJECT

def add(numbers):
	if numbers == "":
		return 0

	numbers = numbers.replace("\n", ",")

	if not "," in numbers:
		return int(numbers)

	numbers = numbers.split(",")
	numbers = map(int, numbers)
	return sum(numbers)

################################### TESTS

# ex 1
def test_empty_string_returns_0():
	assert add("") == 0

def test_single_number_converts_to_number():
	assert add("1") == 1
	assert add("5") == 5

def test_two_numbers_get_added():
	assert add("1,2") == 3

# ex 2 - oops worked right away
def test_arbitrary_numbers_get_added():
	assert add("1,2,3") == 6

# ex 3
def test_newlines_also_separate():
	assert add("1\n2,3") == 6