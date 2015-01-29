#!/usr/bin/python -tt

# String Calculator - Interactions
# http://osherove.com/tdd-kata-2/

############################ TEST SUBJECT

import pytest
import re
from mock import Mock

class Calculator:
	def __init__(self, logger = None):
		self.logger = logger

	def add(self, numbers):
		if numbers == "":
			total = 0

		else:
			# read delimiter meta
			delimiters = [","]
			if numbers[:2] == "//":
				numbers = numbers[2:]

				(delimiters, nl, numbers) = numbers.partition("\n")

				if len(delimiters) > 1:
					if not "][" in delimiters:
						delimiters = [delimiters[1:-1]]
					else:
						delimiters = delimiters[1:-1].split("][")

				else:
					delimiters = [delimiters]

			# escape for regex split
			for specialRegexChar in list("\\*+.?(){}[]^$|"):
				delimiters = list(map(lambda d: d.replace(specialRegexChar, "\\" + specialRegexChar), delimiters))

			delimiters.append("\\n")

			numbers = re.split("|".join(delimiters), numbers)
			numbers = list(map(int, numbers))

			if any(n < 0 for n in numbers):
				raise Exception("negatives not allowed: " + str(list(n for n in numbers if n < 0)))

			total = sum(n for n in numbers if n <= 1000)


		if not self.logger is None:
			self.logger.write(total)

		return total

############################## KATA-2 TESTS

# ex 1
def test_logger_writes_result():
	logger = Mock()
	calcer = Calculator(logger)

	total = calcer.add("1,2,3")

	logger.write.assert_called_with(6)


############################## KATA-1 TESTS

def add(numbers):
	# for backwards compatibility :p
	calcer = Calculator()
	return calcer.add(numbers)

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

# ex 7
def test_any_length_delimiter():
	assert add("//[***]\n1***2***3") == 6

# ex 8-9
def test_allow_multiple_delimiters():
	assert add("//[*][%]\n1*2%3") == 6