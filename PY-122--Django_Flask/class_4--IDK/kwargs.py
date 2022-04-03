
"""
Pass the following dictionary as a key word argument called pemdas and print
out all of its keys and values
"""

def kwargs_func(**pemdas):
	print(pemdas)

kwargs_func(
		P='Parenthesis', E='Exponents', 
		M='Multiplication',D='Division', 
		A='Addition', S='Subtraction'
	)
