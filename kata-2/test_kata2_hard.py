#!/usr/bin/python -tt

# String Calculator - Interactions
# http://osherove.com/tdd-kata-2/

import pytest
from mock import Mock

import sys
import io
from Calculator import Calculator

import scalc

########################## HARD KATA-2 TESTS

input_index = -1

def setup_function(function):
	backup = sys.stdout
	f = io.StringIO()
	sys.stdout = f

def teardown_function(function):
	sys.stdout.close()
	sys.stdout = backup

# ex 1
def test_result_also_to_stdout():
	calcer = Calculator()

	total = calcer.add("1,2,3")
	out = sys.stdout.getvalue()

	assert total == int(out)

# ex 1b

def test_scalc_cli_with_input():
	scalc.get_input = lambda x: ""
	scalc.main("1,2,3")

	out = sys.stdout.getvalue()

	assert "6" in out

# ex 2
def input_replacer(text):
	global input_index

	input_index += 1
	return ["1,2", "5", ""][input_index]

def test_scalc_cli_with_multiple_input():
	scalc.get_input = input_replacer
	scalc.main("1,2,3")

	out = sys.stdout.getvalue()

	assert "6" in out
	assert "3" in out
	assert "5" in out