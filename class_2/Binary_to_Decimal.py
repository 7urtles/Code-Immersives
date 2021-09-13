

def binary_to_decimal():
    # Get binary input from user
    user_input = input("Enter a binary number to conver to decimal: ")

    # Convert input to string
    binary_list = str(user_input)

    # Split the string into a list
    binary_list = list(binary_list)

    # Reverse the list
    binary_list_reversed = binary_list[::-1]
    
    # Variabes to sore our working total, and current position in the list
    total = 0
    position_in_list = 0

    # Iterate the reversed list
    for i in binary_list_reversed:

        # If the current digit is a 1
        if i =='1':

            # Increase the total by 2 to the power of the current digits position
            total = total + (2 ** position_in_list)
        
        # Adjust our position in the list
        position_in_list += 1

    # Display the total
    print("Answer: {}".format(total))


binary_to_decimal()