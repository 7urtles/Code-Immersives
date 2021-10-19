# Create a function that is passed a list containing 5 different number

# Sort this list without using methods

number_list = [1,2,3,4,5]

def sorting_function(input_list):
    highest = 0
    solution = []
    while input_list:
        highest = input_list[-1]
        for i in input_list:
            if i > highest:
                highest = i
        solution.append(highest)
        input_list.remove(highest)
    print(solution)
print(f'Starting list: {number_list}')
sorting_function(f'Here is your sorted list: {number_list}')

