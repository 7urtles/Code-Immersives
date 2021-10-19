# Create a function that takes a list of numbers and returns back a list of booleans
#
# If the value is less that 55 substitute it for False, otherwise make it True
grades = [56,84,95,53,51,42,32,78,64,34,99,65,21]

def who_passed(edited_grades):
    # Iterate the grades in the list
    for number in range(0, len(edited_grades)):
        # If below 55 fail em
        if edited_grades[number] < 55:
            edited_grades[number] = False
        # Otherwise they pass
        else:
            edited_grades[number] = True
    print(edited_grades)
    return edited_grades

who_passed(grades)