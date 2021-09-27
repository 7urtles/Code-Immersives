# Write a function called isEven() that will take in a number 
# The function should return whether the number is even or not

def isEven(number):
    result = False
    # If the number divided by two has no remainder
    if number % 2 == 0:
        # If it is even set 'even' to True
        result == True
    # Print the result
    print(f'The number {number} is even: {result}')
    
isEven(9)


