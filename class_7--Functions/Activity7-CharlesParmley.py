'''
1. Create a function named add that expects two arguments.

2. Return the sum of those two arguments.

3. Repeat this process for Subtracting, Multiplying, and Dividing.
'''


# 1. Sum of two numbers
def add(num1, num2):
    total = num1 + num2
    print(f'The sum of {num1} and {num2} is: {total}')
    return total

add(2,5)



# 3. Difference of two numbers
def subtract(num1, num2):
    total = num1 - num2
    print(f'The difference of {num1} and {num2} is: {total}')
    return total

subtract(2,5)



# 4. Product of two numbers
def multiply(num1, num2):
    total = num1 * num2
    print(f'The product of {num1} and {num2} is: {total}')
    return total

multiply(2,5)



# 4. Division of two numbers
def divide(num1, num2):
    total = num1 / num2
    print(f'The result of {num1} divided by {num2} is: {total}')
    return total

divide(10,5)
