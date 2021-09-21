# LOOPS
'''
- An Aplication sometimes needs to perfrom repetitvive actions like:
    + Getting the sum of all the values in a list
    +Getting the average of all the numbers in a list
    + Entering Multiple Data Entries
    + A shopping list (scanning through the list and getting the item
        one by one)

When a program repeatedly runs a set of statements, it is reffered
    to as a loop, iteration or repetition structure.
    + While Loops
    + Do-While Loops
    + For Loops
    + Nested Loops

WHILE Looops are known as Conditional Loops

FOR Loops are known as Counter Controlled Loops

'''
# Similar to conditionals, loops rely on a True/False condition to end
# The loop run indefinitely until a certain condition is met
# Loops can be run for a desired length, or condition is specified

# WHILE loops are constructed as such:
while True: # <-- the 'True' is the condition. The loop will as long as the condition is true
    print('oops in a loop')
    break # <-- the above loop will run indefinitely so we use break to escape the loop

# Other conditionals may be used:
while 1 < 2:    # 1 < 2 will always return True
    print('looping with conparisons')
    break

# Adding a counter can help loop an amount of times
counter = 3 # The amount of times to loop
while counter > 0: #<------As long as counter is above zero, the loop will run.
    print(counter)
    counter -= 1   # Subtracting 1 to counter each loop will decrease it
                   # When the counter reaches 0, the loop will exit because
                    # The condition 0 > 0 will evaluate to false

# The same can be done counting upwards
counter = 0 # Initialeze the counter at zero because we will count up.
while counter < 5: #<------As long as counter is below 5, the loop will run.
    print(counter)
    counter += 1   # This time increasing the counter



# The number value can be replaced with the length of an item
bag = ['apples', 'bananas', 'cherries'] # <--- We will travel this list
counter = 0
while counter < len(bag): #<-- Now making the second position of the conditional
    # set a fruit variable equal the bags index of counter
    fruit = bag[counter] 
    print(fruit)
    counter += 1