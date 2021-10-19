# CONDITIONALY STATEMENTS

'''

1. The basic decision statements in computer is a selection structure

2. The decision is described to computer as a conditional statement that
   can be answered True or False

3. Python provides the following conditional statements:

    -if
    -if/else
    -if/elif/else
    -nested if/else

'''




# [IF STATEMENT]:
# ---------------

# The 'if' conditional is used to run code, if a condition is true or false
# Example:
if 1 < 2:   # This will check if 1 < 2 evaluates to true,
            #   and if so will run the indented code below.
    print("1 is less than 2")




# [ELSE STATEMENT]:
# -----------------

# The 'else' statement may be added below it,
#   and will run the code below it when the 'if' statement fails

if 1 > 2: # <-- checks if 1 is greater than 2.
    print('1 is greater than 2') # <-- it is not, 
                                 # so this print() will not run

else:   # the if condition was not evaluated to true,
        # so now the code in the 'else' statement will run.
    print('1 is not greater than 2')




# [ELIF STATEMENTS]:
# ------------------
# 'elif' statements are used to add multiple conditions 
#   to if/else code blocks.


if 1 > 1: # <-- This evaluates to false so python moves
            #   to the elif statement.
    print('1 is greater to 1')

elif 1 == 1: # <-- The 'elif' statement evaluates to True,
                #   resulting in the execution of it's code.
    print('1 is equal to 1')

else:   # <-- Because the 'elif' evaluated to True and executed its code,
        #       the 'else' statement is skipped.
    print('1 is less than 1')