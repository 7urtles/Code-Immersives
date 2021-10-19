# Underscores '_' may be used to format commas ',' into integers
# It places a marker in the object to be filled with the value specified:
number = 1_000_000
print(f'{number:,}')

# In line if statements:
good = True
message = 'Good' if good == True else 'Bad'
print(message)


# -----[ENUMERATE]-----
a_list = ['a','b','c','d']
# enumerate() passes a tuple containing the index number and it's corresponding item from the list
for grade in enumerate(a_list):
    print(grade)

# access the either by index:
for grade in enumerate(a_list):
    print(grade[0], grade[1])

# or by unpacking the tuple during the statement:
for index, grade in enumerate(a_list):
    print(index,grade)



# -----[EXTRACTING VALUE]-----
cards = ('a',1,2,3,4,5,'g')
# the *_ operator signifies the operation of assignments is over when it is reached
item1, item2, item3, *_ = cards
print(item1, item2, item3)

# using '*' + 'list_name' will create a list with the items found.
letter_a, *numbers = cards
print(letter_a, numbers)

# if more assignments are declared after the *list_name,
#   *list_name will leave room for them to be assigned
letter_a, *numbers, letter_g = cards
print(letter_a, numbers, letter_g)




# -----[FOR ELSE]-----
num_list = [1,2,3,4,5,6,7,8]
# Will execute code in an else block if the loop completes without being broken
my_number = 9
for number in num_list:
    # The number is matched
    if my_number == number:
        print('Number Matched')
        # This break exits the loop, preventing 'else:' code from running
        break
# if the for loop completes it's cycles this code executes
else:
    print('Number not found')