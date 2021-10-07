# -----[List Comprehension]-----

# A faster was of building a lists with for loops
# Its syntax is slightly different and more compact than for loops
a_list = ['a','b','c']
new_list = [item for item in a_list]
print(new_list)

# Conditionals my be added:
new_list = [item for item in a_list if item == 'a'] # <--- The if contional added
print(new_list)

# Operations may be done at the begenning of the statement
new_list = [item+'a' for item in a_list]
print(new_list)

[new_list.append(item) for item in new_list]
print(new_list)

stuff = [1, 2, 3, 4, 5]

num = 0

for i in stuff:
    num += 1

[num+1 for item in stuff]
print(num)