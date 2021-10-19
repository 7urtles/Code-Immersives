# TUPLES
'''
Created using ()

Properties: Immutable, you cannot replace items using position
Example (THIS WILL FAIL): 
    some_tuple[0] = 'something'

First item needs a comma after the item in the tuple,
otherwise the objects data type will default to its
contents.
'''
# This will return a tuple type
some_tuple = ('thing',)
print(type(some_tuple))

# This will return a string type
some_tuple = ('test')
print(type(some_tuple))

# Tuple items can be added (or multiplied) but not using .append()
some_tuple = ('item',)
some_tuple += ('replaced',)
print(some_tuple)

# Tuple items cannot be removed
""" 
THESE WILL FAIL
some_tuple -= some_tuple[1]
some_tuple -= 'item'
some_tuple -= 'item', 
"""