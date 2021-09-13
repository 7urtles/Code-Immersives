def decimal_to_binary():
    # Get an initial decimal format number from the user
    user_input = input("\nEnter a number to be converted to binary: ")
    binary_number = ''

    # Make sure input is an integer
    user_input = int(user_input)
    temp = user_input

    # list holding even numbers doubling by 2
    doubling_numbers = []

    # Counter to help get only even numbers
    count = 0

    # A number that increases by its self multiplied by 2
    doubled_number = 1

    # As long as our number increasing by (its self times 2)
    # is less than or equal to the users number
    while doubled_number <= temp:

        # if the counter is an even number
        if count % 2 == 0:
            # add the number to our list
            doubling_numbers.append(doubled_number)
            # double the number
            doubled_number *= 2

        # increase the counter
        count += 1
    
    # reverse the list
    doubling_numbers = list(reversed(doubling_numbers))

    # iterate the doubling_numbers list
    for i in doubling_numbers:

        # if the current number is less than the users initial input
        if i <= temp:
            # add a '1' character to the binary string
            binary_number += "1"
            # subtract the largest number from the list from the users initial input
            temp -= i
        
        else:
            # add a '0' to the binary variables string
            binary_number += "0"

    # Display the results to the user
    print("Binary Output: {}".format(binary_number))

decimal_to_binary()