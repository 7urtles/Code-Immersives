"""
Write a function that will alternate between adding and subtracting all of the numbers

sent as arguments to a function called alt_calc.

Send the following arguments to the function:

Example 1 - print(alt_calc(10,3,4))

Example 2 - print(alt_calc(20,16,6,8,14,3))
"""

numbers = (1,2,3,4,5,6,7,8,9)

def something(*args):
	current = 0
	# iterate args
	for num,iter in enumerate(args):
		# for even iterations
		if num % 2:
			# add the number
			current+=num
		# otherwise subtract it
		else: current-=num
	return current

print(something(1,2,3,4,5,6,7,8,9))
