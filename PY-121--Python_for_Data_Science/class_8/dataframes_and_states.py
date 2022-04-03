'''
Additional assignment: 
    Use pandas to create a dataframe storing states and square mileage.
    Requested Results:
       1. 5 Summary Statistics from data (mean, median, mode, stdev, ...). 
       2. Plot the areas in a histogram using matplotlib.
'''

import matplotlib.pyplot as plt
import pandas as pd

# pandas csv to dataframe conversion
data = pd.read_csv('state-areas.csv')
# uncomment if needed
# print(type(data))

# displaying summary statistics
print(data['area (sq. mi)'].describe())

# plotting histogram
data.plot()
plt.show(block=True)