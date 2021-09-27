# Write a function called isEven() that will take in a number 
# The function should return whether the number is even or not

def isEven(number):
    even = False
    # if the number divided by two has no remainder
    if number % 2 == 0:
        even == True
    print(f'The number is even: {even}')

isEven(9)
