# Given a list of grades (integers), calculate the standard deviation

# Return the list with all exam values updated by itself plus the standard deviation. 

# Include something that states that if adding the standard deviation to the current
#   exam score brings the total over 100, then that total becomes 100
import statistics

test_list = [88,78,96,84,65,72,95,81,82,60,73]

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
        
    print(adjusted_grades)

number_standard_deviation_sum(test_list)