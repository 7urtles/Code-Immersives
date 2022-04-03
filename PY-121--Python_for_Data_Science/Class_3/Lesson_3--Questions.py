# Answer the following:
# 1 - List the months where sales are greater than or equal to 150
# 2 - Return a tuple of all months and sales amounts greater than or equal to 300
# 3 - List all 3 consecutive month periods where sales are below 500
# 4 - Include the total sales amount for answer 3

sales = {'Jan': 150, 'Feb':200, 'Mar': 175,
        'April': 75, 'May': 80, 'Jun': 300,
        'July': 250, 'August':130, 'September': 195,
        'October': 75, 'November': 120, 'December': 400}


print("\nQuestion 1")
print([month for month,amount in sales.items() if amount >= 150])
print("\n\nQuestion 2")
print(tuple(month for month,amount in sales.items() if amount >= 300))
print("\n\nQuestion 3")
[print(list(sales.keys())[num:num+3]) for num,_ in enumerate(sales.items()) if sum(list(sales.values())[num:num+3]) < 500 and len(list(sales.values())[num:num+3])==3]
print("\n\nQuestion 4")
[print(list(sales.items())[num:num+3][0]) for num,_ in enumerate(sales.items()) if sum(list(sales.values())[num:num+3]) < 500  and len(list(sales.values())[num:num+3])==3]
