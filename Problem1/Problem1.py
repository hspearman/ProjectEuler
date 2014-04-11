__author__ = 'Hannah'

def get_sum_of_multiples():
	result = 0
	for i in range (0, 1000):
		multipleOfThree = (i % 3) == 0
		multipleOfFive = (i % 5) == 0

		if (multipleOfThree and multipleOfFive):
			result += i
		elif (multipleOfThree):
			result += i
		elif (multipleOfFive):
			result += i

	return result

print(get_sum_of_multiples())
