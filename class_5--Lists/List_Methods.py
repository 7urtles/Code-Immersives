# Using List Methods
'''
Python uses Object Oriented Programming (OOP). Everything is considered an object.
All objects have two things

    1: Properties (props)
    2: Behavior (methods/functions)
        Method Usage:
            Either: Object.method() or method(Object)
'''

# Methods
'''
Methods take input, process the input, give an output
'''

    # len() 
    # Returns the length of an object.
    #       Usage: len(some_list)
    #       Returns: an integer represending the length

    # type() 
    # Returns the type of an object.
    #       Usage: type(some_list)
    #       Returns: the type of the give object

    # remove() 
    # Remove first item in a list.
    #       Usage: some_list.remove()
    #       Returns: the list without the first item

    # pop() 
    # Remove last item in a list, can store that item
    #       Usage: some_list.pop() OR last_item = some_list.pop()
    #       Returns: the list without the last item

    # clear() 
    # Remove all items from a list
    #       Usage: some_list.clear()
    #       Returns: an empty list

    # copy() 
    # copy all items to a new list
    #       Usage: new_list = some_list.copy()
    #       Returns: a copy of the original list

    # sort() 
    # sort items in a list
    #       Usage: some_list.sort()
    #       Returns: a sorted version of the original list
    #       Can sort backwards using some_list.sort(reverse=True)

    # reverse() 
    # reverse items in a list
    #       Usage: some_list.reverse()
    #       Returns: a reversed version of the original list

    # count() 
    # count how many times an item occurs in a list
    #       Usage: some_list.count('item')
    #       Returns: number of times the string occurs

