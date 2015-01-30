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
def test_scalc_cli():
	scalc.main("1,2,3")

	out = sys.stdout.getvalue()

	assert out.rstrip().endswith("6")
