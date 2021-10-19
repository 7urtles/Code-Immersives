# Write a function that does what the List.max() method does
# Function must return largest item of list without using .max
number_list = [1,2,3,4,5]

def sorting_function(input_list):
    highest = 0
    for i in input_list:
        if i > highest:
            highest = i
    print(f'The highest number is: {highest}')

sorting_function(number_list)
