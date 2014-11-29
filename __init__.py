#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
	Verificate bank card by Luhn algorithm.
"""

class BankCard(object):
	"""
		Main class.
	"""

	def modify(self, num):
		""" Modify a number."""

		l = self.IntList(num)[::-1]

		s = 0
		for k, v in enumerate(l):
			if k % 2 == 0:
				s += v
			else:
				if 2 * v > 9:
					s += (2 * v) - 9
				else:
					s += 2 * v

		return s % 10 == 0

	def IntList(self, num):
		""" Convert long int into int list."""
		return map(int,list(str(num)))

examples = [
	356406010024817,
	358973017867744,
	356827027232781,
	306406010024817,
	358973017867754
]

bc = BankCard()

for v in examples:
	print v, bc.modify(v)