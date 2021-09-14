# Updating a list

some_list = ['this', 'is', 'a', 'list', 'of', 'words']

print(some_list)

# Refer to the items index in the list, and re-assign it

some_list[1] = 'isnt'

some_list[4] = 'holding'

some_list[5] = 'integers'

# Using slices to replace list items
some_list = ['a','new','list']
some_list[0:3]='test','this','out'
print(some_list)