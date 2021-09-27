

# Day 11 Activities

# Write a function called isEven() that will take in a number 
# The function should return whether the number is even or not
def isEven(number):
    result = False
    # If the number divided by two has no remainder
    if number % 2 == 0:
        # If it is even set 'result' to True
        result = True
    # Print the result
    print(f'The number {number} is even: {result}')
isEven(9)


# Write a function called isSorted which will be passed in a list of numbers
# The function should deterimine if the list needs to be sorted or is already sorted
# Return a boolean value

def isSorted(number_list):
    sorted = True
    # Check first number in the provide list of numbers
    current_number = number_list[0]
    # Iterate the list
    for number in number_list:
        # if the number is greater or equal to the previous number
        if number >= current_number:
            # Set the new number for next iteration of loop
            current_number = number
        # If the number is less than the previous one
        else:
            # Set the sorted value to False
            sorted = False
    print(f'The list is sorted: {sorted}')

isSorted([0,1,2,3,1])