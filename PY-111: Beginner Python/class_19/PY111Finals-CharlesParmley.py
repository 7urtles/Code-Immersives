# Given two int values return their sum. If the are the same return the square of their sum
def sum_squared(x,y):
    if x != y:
        return x + y
    return (x+y)**2
x = 2
y = 2
print(f"#16 sum_squared result: {sum_squared(x,y)}")


# Write a functions takes in a list and uses list comprehension to generate and
#   return a list of values consisting of each item cubed.

def items_cubed(input_list):
    return [num**3 for num in input_list]
print(f"#17 List items cubed results: {items_cubed([1,2,3,4])}")


# Given an int array with a length of 3, return True if it contains
#  a 2 or a 3
def contains_two_or_three(an_array):
    if 2 in an_array or 3 in an_array:
        return True
    return False
print(f"#18 Is there a 2 or a three results: {contains_two_or_three([1,2,3])}")


# Return the number of even integers in an array
def number_of_evens(some_list):
    total = 0
    [total := total+1 for number in some_list if number%2==0]
    return total
print(f"#19 How many are even results: {number_of_evens([1,2,3,4])}")


# Given 3 int values return their sum
#   If one of the values is 13, it does not count and neither do the numbers
#   after it.
def lucky_sum(a,b,c):
    numbers = [a,b,c]
    total = 0
    for num in numbers:
        if num == 13:
            return total
        total += num
    return total

print(f"#20 Lucky Sum results: {lucky_sum(2,13,3)}")