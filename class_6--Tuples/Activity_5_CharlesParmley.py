'''
a. Create a tuple with different data types.

b. Create a tuple with multiple values and print the last item.

c. Get the 4th element from the front, and the 4th element from the end.

d. find the length of a tuple.
'''
# Answer a
some_tuple = ('string', 5)

# Answer b
some_tuple = ('these', 'are', 'multiple', 'values', 'in', 'a', 'tuple')
print(some_tuple[-1])

# Answer c
some_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print('4th element in the tuple: ', some_tuple[3], '\n4th element from the end:', some_tuple[-4] )

# Answer D
print(len(some_tuple))