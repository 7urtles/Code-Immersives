# Given a list of grades (integers), calculate the standard deviation
#
# Return the list with all exam values updated by itself plus the standard deviation. 
#
# Include something that states that if adding the standard deviation to the current
#   exam score brings the total over 100, then that total becomes 100


import statistics

grades = [56,84,95,53,51,42,32,78,64,34,99,65,21]



def number_standard_deviation_sum(grade_list):
    adjusted_grades = []
    # Find standard deviation of the provided list
    standard_deviation = statistics.stdev(grade_list)
    # Iterate the given list
    for grade in grade_list:
        # Add the standard deviation to the grad
        adjusted_grade = grade + standard_deviation
        # Convert it into and integer
        adjusted_grade = int(adjusted_grade)
        # If the total is over 100, adjust it to 100 (The max possible grade)
        if adjusted_grade > 100:
            adjusted_grade = 100
        # Put the adjusted grade into a new list
        adjusted_grades.append(adjusted_grade)
    print(f"Starting grades: {grade_list}")
    print(f'Curved grades: {adjusted_grades}')
    return grade_list, adjusted_grades

grade_list, adjusted_grades = number_standard_deviation_sum(grades)




# Create another function that gets me the average value fo the original exam grades
def number_standard_deviation_sum(grade_list):
    # Find the mean of the curved grades
    before_curve_average = statistics.mean(grade_list)
    # Round to an integer 
    before_curve_average = int(before_curve_average)
    print(f'Average grade BEFORE curve: {before_curve_average}')
    return before_curve_average

before_curve_average = number_standard_deviation_sum(grade_list)





# Write a function that returns the average value of the curved exam grades
def average_of_curves(curved_list):
    # Find the mean of the curved grades
    after_curve_average = statistics.mean(curved_list) 
    # Round to an integer 
    after_curve_average = int(after_curve_average)
    print(f'Average grade AFTER curve: {after_curve_average}')
    return after_curve_average
after_curve_average = average_of_curves(adjusted_grades)






# Create a function that takes a list of numbers and returns back a list of booleans
#
# If the value is less that 55 substitute it for False, otherwise make it True
def who_passed(grades):
    pass_or_fail = []
    # Iterate the grades in the list
    for number in range(0, len(grades)):
        print(grades[number])
        
        # If below 55 fail em
        if grades[number] < 55:
            print('Fail')
            pass_or_fail.append(True)
        # Otherwise they pass
        else:
            print('Pass')
            pass_or_fail.append(False)

    print(pass_or_fail)
    return pass_or_fail

pass_or_fail = who_passed(grades)







# Create a function that takes in a list of grade pass/fails
#   and finds how many people failed the class
def count_the_failures(pass_or_fail):
    good_students = 0
    failures = 0
    is_a_failure = True

    for failure in pass_or_fail:
        if failure == is_a_failure:
            failures += 1
            continue
        good_students += 1

    print(f'There are {good_students} passing,\n  and {failures} failing.')
    return good_students, failures

good_students, failures = count_the_failures(pass_or_fail)







# Given a list of integers representing grades(curved or not), print a 
#   message stating how many people passed or failed (55 beind a passing grade).

def count_fails_from_integers(list_of_grades):
    good_students = 0
    failures = 0
    lowest_passing_score = 55
    for grade in list_of_grades:
        if grade < lowest_passing_score:
            failures += 1
            continue
        good_students += 1
    print(f'There are {good_students} passing,\n  and {failures} failing.')
    return good_students, failures

good_students, failures = count_fails_from_integers(grades)