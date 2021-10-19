'''
1. Create dictionary named car.

2. Give it a brand, model, and year.
    -It should describe a 1964 Ford Mustang.

3. Print the model of the car.

4. Perform dictionary methods on the dictionary object,
   and explain their effects.

5. Submit to Populi and Github
'''

# Answer 1
car = {}

# Answer 2
car['brand'] = 'Ford'
car['model'] = 'Mustang'
car['year'] = 1964

# Answer 3
print(f"The cars model is a {car['model']}\n")

# Answer 4
car.update({'condition':'great'})

print(f"Using the .update() method to insert a key/value pair \n containing the condition of the car results in: \n\n{car}")