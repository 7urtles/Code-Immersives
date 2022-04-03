import string
import pandas as pd


# It doesnt say to print the Series before the indexing,
#   so steps are combined and the result returned

# working from a dictionary comp allows setting
#  the index positions from the dict values
#  when creating a series. 
def ascii_index(ascii_set:list)->pd.Series:
    return pd.Series({ord(letter):letter for letter in ascii_set}).loc[72]

# item with an ascii key of 72 from the Series
print(ascii_index(string.ascii_uppercase))