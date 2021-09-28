# Create a function that generates a random list
# It should take in a number that is the size of the list.
# The values passed in should be between 20 and 78.

from random import randrange

def random_list_generator(list_length = 5):
    result_list = []
    # Iterate a specified amount of times
    for number in range(0,list_length):
        # Only add random numbers between 19 and 78
        result_list.append(randrange(20,78))
    print(result_list)

random_list_generator(1000)