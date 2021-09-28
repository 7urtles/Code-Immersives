# Write a function that will take in an integer, and create a list of the size passed in as an argument.
# Populate that list with random numbers from 0-1024
# Use the getrandbits() method

# importing the necessary function from the module
from random import getrandbits
def random_number_maker(list_length):
    # List to hold generated numbers
    random_number_list = []
    # Run the random generator 5 times
    for iterations in range(0,list_length):
        # Create a random number
        random_number = getrandbits(10)
        # Append it to the list
        random_number_list.append(random_number)
    print(random_number_list)

random_number_maker(5)
    
