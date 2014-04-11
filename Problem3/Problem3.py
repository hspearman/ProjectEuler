__author__ = 'Hannah'

# Given an odd number, tests whether or not it is a prime number
def is_prime_number(number):
	# Iterate through every possible odd factor
	for possible_factor in range(3, number, 2):
		# If something divides evenly into the number, then it is NOT prime
		if number % possible_factor == 0:
			return False

	# If nothing divided evenly into the number, then it is prime
	return True

# Recursive version of finding factors.
# Deprecated because it exceeds the maximum recursion depth for larger numbers
#def find_factors(a, b):
#	# Base case. Everything is divisible by 1, so stop here.
#	if b == 1:
#		return [1]
#	# If the number divides evenly into the number, then record it and keep looking for factors
#	elif a % b == 0:
#		return [b] + find_factors(a, b - 1)
#	# Else it's not a factor. Keep looking for more factors.
#	else:
#		return find_factors(a, b - 1)

# Finds the larger odd factors of a given number
# (ex. 3 * 7 = 21. 7 is the larger odd factor, so it's part of the returned list)
def find_odd_factors(number):
	odd_factors = []

	# Iterate through every possible odd factor starting from the largest odd number under n.
	# Continue  that's less than the square root of n.
	# We only check up to sqrt(number) to avoid redundantly checking a pair of factors twice
	# For example, suppose number = 21 and i = 7. 3 is a factor of 21 (3 * 7 = 21) so we record it.
	# If we exceed sqrt(21), we will
	possible_factor = 3
	possible_factor_squared = 9
	while possible_factor_squared < number:
		# If something divides evenly into the number, then it is a factor so record it
		if number % possible_factor == 0:
			odd_factors.append(possible_factor)

		# Increment by 2 to skip over even numbers
		possible_factor += 2

		# Calculate the square for the new possible factor
		possible_factor_squared = possible_factor * possible_factor

	return odd_factors


# Find the odd factors for this number (since even numbers can't be prime)
number = 21
factors = find_odd_factors(number)

# Iterate through the list of factors and find the largest prime factor
max_prime_factor = -1
for item in factors:
	# Check if this factor is prime
	b_is_prime_number = is_prime_number(item)

	# If it's prime and it's the largest prime factor we've seen, record it
	if b_is_prime_number and item > max_prime_factor:
		max_prime_factor = item

print(max_prime_factor)


