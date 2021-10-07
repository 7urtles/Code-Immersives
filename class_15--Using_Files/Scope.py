# -----[SCOPE]-----
# Scopes are different levels of visibility in a program
# Scope has three levels
#       -Global
#       -Local
#       -Block


# Global mean that everything in the script can access it
# An example is a variable defined outside of a function or class:
global_variable = 10
print(global_variable)


# Local means that the variable is only accessible within the code block that contains it
# Local variables are generally within and 'local' to a function:
def i_have_scope():
    local_variable = 0
    print(local_variable)
i_have_scope()
# It cannot be accessed outside of the function:
# print(local_variable) will fail. print() can not find the variable outside of it's scope.


# However the function can access the global variable:
def accessing_globals():
    print(global_variable)
accessing_globals()