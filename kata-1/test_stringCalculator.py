#!/usr/bin/python -tt

# String Calculator
# http://osherove.com/tdd-kata-1/

############################ TEST SUBJECT

import pytest

def add(numbers):
	if numbers == "":
		return 0

	delimiter = ","

	if numbers[:2] == "//":
		delimiter = numbers[2]
		numbers = numbers[4:]

	numbers = numbers.replace("\n", delimiter)

	numbers = numbers.split(delimiter)
	numbers = list(map(int, numbers))

	if any(n < 0 for n in numbers):
		raise Exception("negatives not allowed: " + str(list(n for n in numbers if n < 0)))

	return sum(n for n in numbers if n <= 1000)

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
def test_newlines_also_separates_input():
	assert add("1\n2,3") == 6

# ex 4
def test_delimiter_prefix():
	assert add("//;\n1;2") == 3

# ex 5
def test_negative_number_throws():
	with pytest.raises(Exception) as ex:
		add("1,2,-5")

	assert '-5' in str(ex.value)

def test_negative_can_be_delimiter_without_exception():
	assert add("//-\n1-2") == 3

# ex 6
def test_numbers_above_1000_are_ignored():
	assert add("2,1001,1") == 3