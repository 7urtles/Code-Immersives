# Write a function that given a list prints out all values in that list
some_list = ['this','is','a','list']
def list_as_input(list):
    for word in list:
        print(word)

list_as_input(some_list)


# Write a function that takes in one integer as a parameter and will print out your name
# as many times as specified by the parameter
iterations = 5
def name_repeater(number):
    counter = 0
    name = 'Charles'
    while counter < number:
        print(f'My name is {name}')
        counter += 1
name_repeater(iterations)