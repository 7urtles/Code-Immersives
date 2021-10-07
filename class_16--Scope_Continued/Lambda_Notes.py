
#-----[LAMBDAS]-----
# 
# Lambdas can be thought of as one time use functions

# They are defined using the 'lambda' keyword. Similar to how 'def' is for functions
# Syntax is as such:
lambda x : 1 + x

# the lambda function can be saved to a variable
my_lambda = lambda x : x + 2

# and then called with parameters
print(my_lambda(1))

# Getting results immedately by...
#   Wrapping the lambda in parenthesis: 
#       (lambda x : x + 1)
#   Then passing the lamba a value or variable as an arguement: 
#       (lambda x : x + 1)(2)
number = 2
result = (lambda x : 2 + x)(number)


# If lamdas can only contain one expression and use a variable,
# what is the use case of using them preferred over updating a variable
# with an expression?

# When is a lamba usage:
lambda x : x + 2

# benefecial over an expression?:
x = x + 2

#   ?????