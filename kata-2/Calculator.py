import sys
import re

class Calculator:
	def __init__(self, logger = None, log_ex_service = None):
		self.logger = logger
		self.log_ex_service = log_ex_service

	def add(self, numbers):
		inputNumbers = numbers

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


		if self.logger is not None:
			try:
				self.logger.write(total)
			except:
				if self.log_ex_service is not None:
					self.log_ex_service.error("Error with input: " + inputNumbers + "\n" + str(sys.exc_info()[0]))

		print(total)

		return total