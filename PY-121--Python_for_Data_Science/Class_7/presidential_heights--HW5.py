

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

'''
Find average height of US presidents.
Plot the heights.
'''

pres_data = pd.read_csv('president_heights.csv').to_numpy()
# Specifying to get a 2d slice of all rows, 3rd column.
# Then let numpy handle getting the mean
print(np.mean(pres_data[:,2]))

# Create bar graph using president number as x-axis and their height as y-axis
plot = plt.bar(pres_data[:,0], pres_data[:,2])
# Showing every x-axis president number
plt.xticks(list(pres_data[:,0]))
# Here ya go
plt.show()

# Sometimes my windows get stuck so:
print('Press q to close!')
plt.waitforbuttonpress(0) 
plt.close('all')
