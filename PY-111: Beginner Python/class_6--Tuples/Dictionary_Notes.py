# DICTIONARIES
'''
Created using {}

Properties: The key value must be immutable.

Dictionaries have a key and a value.
EXAMPLE:
    some_dictionary = {'key':'value'}
'''
# Here is a dictionary
some_dictionary = {'key':'value'}

# Access the value by referencing its key
# This example will print the string: 'value'
print(some_dictionary['key'])

# Keys and values may be different data types
variable = 'something'
some_dictionary = {1:'value', 'key':'value2', variable:5}
print(some_dictionary[variable]) 

# Adding keys/values to a dictionary
some_dictionary = {1:'one', 2:'two', 3:'three'}
some_dictionary['new key'] = 'four'
print(some_dictionary)
