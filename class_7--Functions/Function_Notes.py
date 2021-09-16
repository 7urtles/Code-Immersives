# DICTIONARIES
'''
Created using def someName():

Properties: Is a container for chunks of code that can be called on.

Functions need to be defined, and then called in order to run them.
EXAMPLE:
                       --
    def someName():     |<--This part is the function
        print('hello')  |
                       --    
    
    someName()          <--This part is the function call

'''


# Here is a function printing "hello world"
def myFunction():
    print('hello world')


# To run the function you must call it like with the function name followed by ():
myFunction()


# Functions have place holders for taking input called arguments
def myFunction(content):
    print(content)




# [PASSING DATA TO A FUNCTION]:
# -----------------------------

# Passing data by ASSIGNMENT:
# In order to give the argument data, it may be directly assigned
def myFunction(content='hello world'):
    print(content)



# Passing data by REFERENCE:
# A functions argument may also be defined by passing it an
#   already defined variable.
# The variable is passed to the function inside the call to the function
message = 'hello world'

def myFunction(content):
    print(content)

myFunction(message) #<-- By calling the function with the variable called message
                    #       the functions arguments called content is now equal to
                    #       the contents of message


# MULTIPLE ARGUMENTS are seperated by commas
name = 'Charles'
message = 'says hello'

def myFunction(person, says):
    print(person, says)

myFunction(name,message) # When passing arguments to the function
                         #   arguments are also seperated by commas


# If you call a function with the wrong amount of arguments an error will occur
def myFunction(person, says):
    print(person, says)

myFunction(name) # The function above expects 2 arguments,
                 #     but we call it with one causing an error.

            


# [RETURNING DATA FROM A FUNCTION]:
# ---------------------------------
 
def myFunction():
    return('Hello World') # <-- using the key word 'return' tells the function
                          #        to end the program, and pass the data within
                          #        return back to where the function was called

myFunction() #<-- The result of calling the function is now 'Hello World'
             #   However nothing will be displayed because it is not printed

# This data is now usable by saving the function call to a variable
# Example:
result = myFunction()

# Now printing the variable 'result' should display 'Hello World'
print(result)