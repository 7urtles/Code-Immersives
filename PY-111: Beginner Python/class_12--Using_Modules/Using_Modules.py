# -----[MODULES]-----

'''
In python extra features can be implimented by using modules

Modules are a group of functions and classes put together to acheive a task
There are two kinds of modules:
    - Included
    - Not included
'''

# Included modules can be used right away with this syntax at the top of the file:

#           import "module name here"

# importing the built in python module random is as such:
import random

# it has functions that can be used through dot notation:
random.randint()

# This calls the randint() function from the module 'random'
# Modules typically have multiple functions that can be called

# randint() takes arguments just like range
random_number = random.randint(0,5)
print(random_number)