#!/usr/bin/python -tt

# String Calculator - Interactions
# http://osherove.com/tdd-kata-2/

import pytest
from mock import Mock

import sys
import io
from Calculator import Calculator

########################## HARD KATA-2 TESTS

# ex 1
def test_result_also_to_stdout():
	calcer = Calculator()

	backup = sys.stdout
	f = io.StringIO()
	sys.stdout = f

	total = calcer.add("1,2,3")
	out = sys.stdout.getvalue()

	sys.stdout.close()
	sys.stdout = backup

	assert total == int(out)