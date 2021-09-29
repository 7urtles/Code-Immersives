# -----[Statistics]-----

import statistics
from typing import Match

# A data set for practicing with the module
data = [2,4,5,9,6,4,8,3,5]

# Finding the mean (average number) within our data set
mean = statistics.mean(data)
print(mean)

# Finding mean without the module...
mean = 0
    # Total the numbers
for number in data:
    mean += number
# Divide by length of the data set
mean = mean / len(data)
print(mean)



# Finding the median
median = statistics.median(data)
print(median)


# Finding standard deviation (Bell Curve)
