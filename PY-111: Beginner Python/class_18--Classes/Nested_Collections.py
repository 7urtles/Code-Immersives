def seperator():
    print('\n')
seperator()



# -----[COLLECTIONS inside COLLECTIONS]-----
# Put one inside the other...Seperate collections with ',' like usual

# LISTS in lists
new_list = [ ['inner_list1','item2a'], ['innerlist_2','item2b'] ]
[print(f'First inner list: {item}') for item in new_list]
seperator()

# TUPLES in tuples
new_tuple = ( (0,1), (1,2) )
[print(f'Inner tuple: {item}') for item in new_tuple]
seperator()

# DICTIONARIES in Dictionaries
new_dictionary = { 'dict1':{'item1':True}, 'dict2':{'item1':False} }
[print(f"Inner dictionary item1: {new_dictionary[item]['item1']}") for item in new_dictionary]
seperator()

# DELETING collections
del new_dictionary['dict2']['item1']
print(new_dictionary)
