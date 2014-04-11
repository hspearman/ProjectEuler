__author__ = 'Hannah'

from enum import Enum

LIMIT = 4000000

def get_sum_of_even_fib():
	# Arbitrary starting values for the sequence
	a = 1
	b = 2

	# b is the first even number, so start the sum off with b
	sum_of_even_terms = b

	# Keeps track of every third term
	term_tracker = 0

	# Calculate all fibonacci terms that do not exceed 4 million
	while a <= LIMIT:
		# Calculate the value of c according to the fibonacci sequence
		c = a + b

		# Update the tracker since we've encountered another term
		term_tracker += 1

		# Every third term is an even number, so add it to the sum accordingly
		if term_tracker == 3:
			sum_of_even_terms += c
			term_tracker = 0

		# Set the a and b values for the next fibonacci iteration
		a = b
		b = c

	return sum_of_even_terms

print(get_sum_of_even_fib())