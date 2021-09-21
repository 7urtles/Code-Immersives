# Create a function that takes in 3 integers as parameters. Perform some operation that will compare
    # these values and order the numbers from least to greatest. Return these values as a set
    # in a tuple.

#   This function takes in 3 numbers as input
#   This function will return a sorted Tuple of those 3 numbers passed as input

num1 = 8
num2 = 23
num3 = 5

def smallest_to_largest(num1,num2,num3):
    answer = []
    nums = [num1, num2, num3]
    count = len(nums)
    while len(nums) != 0:
        try:
            smallest = nums.pop(nums.index(min(nums)))
            # print(smallest)
            answer.append(smallest)
            count -= 1
        except:
            pass
    return answer

print(smallest_to_largest(num1,num2,num3))