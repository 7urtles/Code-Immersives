# Write a function that will take in an integer, and create a list of the size passed in as an argument.
# Populate that list with random numbers from 0-1024
# Use the getrandbits() method

# importing the necessary function from the module
from random import getrandbits
def random_number_maker(list_length=5):
    # List to hold generated numbers
    random_number_list = []
    # Run the random generator 5 times
    for iterations in range(0,list_length):
        # Create a random number
        random_number = getrandbits(10)
        # Append it to the list
        random_number_list.append(random_number)
    print(f'Some numbers from 0 up to 1024: {random_number_list}')

random_number_maker(5)




# Create a function that generates a random list
# It should take in a number that is the size of the list.
# The values passed in should be between 20 and 78.

# Import necessary random generating function
from random import randrange

def random_list_generator(list_length=5):
    result_list = []
    # Iterate a specified amount of times
    for number in range(0,list_length):
        # Only add random numbers between 19 and 78
        result_list.append(randrange(20,78))
    print(f'List of random numbers from 19 up to 78: {result_list}')

random_list_generator()


