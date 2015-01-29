#!/usr/bin/python -tt

# String Calculator - Interactions
# http://osherove.com/tdd-kata-2/

import pytest
from mock import Mock

from Calculator import Calculator

####################### SIMPLE KATA-2 TESTS

# ex 1
def test_logger_writes_result():
	logger = Mock()
	calcer = Calculator(logger)

	total = calcer.add("1,2,3")

	logger.write.assert_called_with(total)

# ex 2
class ThrowingLogger:
	def write(self, input):
		raise

def test_failing_log_calls_service():
	#logger = Mock(write=Exception("IO error"))
	logger = ThrowingLogger()
	service = Mock()
	calcer = Calculator(logger, service)

	calcer.add("1,2,3")

	assert service.error.called