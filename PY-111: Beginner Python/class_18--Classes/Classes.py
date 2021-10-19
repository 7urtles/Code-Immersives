


# -----[CLASSES]-----

# Classes help define attributes and behavior for objects
#   create using 'class' similar to how 'def' is for functions

class Class_Name:
    # the __init__() (or 'initialize') method runs automatically and takes the argument 'self'
    # helpful creating objects with 
    def __init__(self,age):
        self.name = "Charles"
        self.age = age

# New save our new object to a variable to create an instance of our class
charles = Class_Name(22) # <-- the () executes the code within our class
# Arguments may be passed while creating a class object.
    # The will be passed to the __init__() method.

# Access the attributes through dot notation
print(charles.name, charles.age)


# Functions can be added to give behavior
class Class_Name:
    def __init__(self):
        self.name = 'Charles'
        self.age = 29
        self.alive = True
    
    # Here we add a function to change the age
    # Pass the self argument so the function can access our 'self' attributes
    def get_older(self):
        self.age += 1
        print(f"Oof, even older: {self.age}")
 
charles = Class_Name()
# Access the function using dot notation
charles.get_older()
# charles.age variable is now increased
print(charles.age)