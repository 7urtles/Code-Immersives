fname = "Charles"
lname = "Parmley"
color = "Blue"
meal = "Sushi"

# f-string
print(f"My first name is {fname}. My last name is {lname}. My favorite color is {color}. My favorite meal is {meal}.")

# Concatenation
print("My first name is " + fname + ". My last name is " + lname + ". My favorite color is " + color + ". My favorite meal is " + meal + ".")

# Argument by position
print("My first name is {0}. My last name is {1}. My favorite color is {2}. My favorite meal is {3}.".format(fname, lname, color, meal))

# Argument by name
print("My first name is {firstname}. My last name is {lastname}. My favorite color is {fav_color}. My favorite meal is {fav_meal}.".format(firstname = fname, lastname = lname, fav_color = color, fav_meal = meal))
