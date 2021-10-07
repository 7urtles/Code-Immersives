#In Python 3.4+ they introduced this short hand notation of creating a list. 

#It's optional, just like lambda and ternary are, it's not recommended like you're working withone that is a Junior because very often these short hand expressions can potentially go over their heads since its a new feature, and the old ones work just fine. 

#Many times in this course, we have been generating Lists, Tuples, and/or Dictionaries in order to solve our problems. 

#We have had to rely on the methods on the object and our python fundamentals in order to generate a new list from values from an old list. 

#For example: What if I had a list of numbers called "originalList", and then wanted to return that list withits values squared and without modifying the actual values that are in the original list. 

#Create the original list: 
'''
originalList = [1, 2, 3, 4, 5]

newList = []
for i in range(len(originalList)):
    newList.append(originalList[i] ** 2)
'''

'''
print(originalList)
print(newList)
'''

#However, believe it or not Python has something that makes it even easier for someone who is a little more experienced with Python to create and interpret new lists from old ones or that you want to generate yourself, and that is called List Comprehension. 

#Python is so good at one liners, and one of those one liners is going to be creating a new list from an old one using list comprehension. Let's take a look at the syntax of how List Comprehension expressions are written. 

'''
                      #Second Arg
newList = [ expression for item in iterable/sequence/collection ]
        #First Arg                      #Third Arg

'''

#What's important to understand is that these one-liners come at a price for new developers, and that is that it utilizes so many fundamental features in one expression that it can be extremely tough to interpret what you're seeing or working with. Think about how many times we have encountered reference errors in our code, and they were all split among several lines. 

#We have debunked, meaning it should no longer be news. Let's take a look at how we could have accomplished the same thing that we did above with List comprehension: 

'''
newList2 = [x**2 for x in originalList]

print(originalList)
print(newList2)

'''

#If this helps makes it more clear: 
    #1. x**2 is the expression
    #2. x within the the "for x in" after the expression "x**2" represents each item in your list
    #3. originalList is the original iterable/sequence/collection that you are referring to. 

'''
li = []

for i in range(10):
    li.append(i)

print(li)
'''

#List Comprehension Expression Equivalent: 
    #1. Expression
    #2 ___ for What is within the "for ____ in" 
    #3 Sequence, Iterable, or Collection

'''
li = [i+2 for i in range(10)]
print(li)
'''

#You can more with List Comprehension. We saw that they both did the same work but that one was a one-liner. This is a Python thing, when you get to Data Science you will see what One-Liners are capable of. 

#You can do more with List Comprehension. We saw what we could do with an expression, list items, and an iterable/collection/sequence. Well, we can also include a 4th argument in that expression as a conditional !!!!

#Let's say that I wanted to generate a new list from a given list with numbers that are even...

#Create a function called evenNums, that takes in a list of numbers as a parameter/argument, and returns a new list with only the even numbers...
    #You can do this using ANYTHING we know. Functions or Lambda, Conditions or Ternary, Lists and Loops or List Comprehension. 



#Review: 
#Lambda and List Comprehension and Ternaries 

#These are the terms for new features in Python3 that allow you to create expressions from statements. The benefit to creating expressions from statements, is that an expression evaluates to some data and some data type all in one line. Therefore, it can be stored in a variable, and/or passed into a function. 

#Example: When we created the add function normally, we did: 

'''
def add(x,y): 
    return x+y
'''

'''
#The lambda equivalent would look like: 
add = lambda x,y: x+y
print(add(3,5))
'''

'''
num = 23
num2 = 12 

# if(num > 21): 
#     return True
# else: 
#     return False

canDrink = True if num > 21 else False
'''

'''
newerList = [x+5 for x in range(0,10)]
print(newerList)
'''

#List Comprehension - Let's you create a list using an expressions or one-liner
#Ternary Operaors - Turned If/Else statements to Expressions
#Lambda - An expression that represents a function in one-line

#What does it mean to be an expression?
 #is a line of code that evaluates to some data or value
    #That data and/or value can be stored as a variable or passed in as an argument into a function

example = [2, 3, 4, 5, 6]

#Notes of Web Dev Stuff NOT Python: 
#When you think of mapping, I come from a javascript, in JS, you have something known as the DOM. The whole purpose of the DOM to to pair/join a function, with some component of your website to make "interactive". 


#With the map function, the map() method will map a function to a list/collection/sequence. 

'''
squared = []
for i in range(len(example)):
    squared.append(example[i] ** 2)
''' 

'''
print(example)
print(squared)
'''
#The map method takes two arguments
    #1. The function you want it to run. 
    #2. The object/collection/sequence you're running the function on. 

''''
#Using Map
squared2 = list(map(lambda x: x ** 2, example))

#Using List Comprehension: 
squared3 = [x**2 for x in example]


print(example)
print(squared2)

'''

#We are going to cover the "filter" methods. Filter works alot like map, except instead of doing some arithmetic expression and mapping to each list item, you will be creating your new list based on a certain condition. Essentially, "filtering" your list. Which is why its called filter()

#Conclude List Comprehensions
#Start Dictionary Comprehensions

#When we want to check if a number is even... We are going to be using the modulus, everytime. 

'''
userInput = int(input("Pick a number, any number: "))
if(userInput % 12 == 0):
    print("That's a multiple of 12 you got there...")
else: 
    print("That's not a multple of 12 you got there...")
'''





dataset = [1, 2, 3, 4, 5, 6, 323, 54, 23, 64]



'''
def evenNumsOnly(dataset = [1, 2, 3, 4, 5, 6, 323, 54, 23, 64]):
    evenNums = []
    for i in range(len(dataset)):
        if(dataset[i] % 2 == 0):
            evenNums.append(dataset[i])
    print(evenNums)
    return evenNums

evenNumsOnly()

'''
'''
#Using Filter
evenNumsOnly2 = list(filter(lambda x: x % 2 == 0, dataset))

#Using List Comprehension
evenNumsOnly3 = [x for x in dataset if x % 2 == 0]

#Ternary Expressions: These change the if/else statements to expressions which can be evaluated in one line, convinient for Python the interpreted language that does everything one line at a time. 

print(evenNumsOnly2)
print(evenNumsOnly3)
'''

'''
#Tuple Comprehension: 
    #This will create a "generator" object
    #A Generator Object is an Object that can be iterated on, looped on.
    #Remember Tuples are Immutable. 
myGenerator = (x for x in dataset)

    #This will create a "list" object
myList = [x for x in dataset]

#Creates a Generator Object

print(myGenerator)
print(type(myGenerator))

#We will cast the Generator Object to a Tuple Object
print(tuple(myGenerator))

#We will confirm the Type of our Tuple Casting here
print(type(tuple(myGenerator)))

#This will print our list
print(myList)

#This will print the type of our list
print(type(myList))
'''



#Dictionary Comprehension
#myDict = {k:v for k,v in dataset}

'''
#We will create a dictionary and populate it with keys and values. 
#The keys will be numbers, and the values will be the key squared.
myDict = {}

for i in range(10):
    if(i % 2 == 0):
        myDict[i] = i**2
    
print(myDict)
'''


'''
newDict = {x:x**2 for x in range(10) if x%2==0}
print(newDict)
'''



'''
#Here we will create a new dictionary object with some keys stored as Strings and values as Numbers/Integers.
fahrenheit = {"t1": 23, "t2": 56, "t3": 98, "t4": 0}

#We are going to use the dictionary method "values()" in order to extract values from our dictionary object. 
    #These values should be returned in the form of a List Object.
print(fahrenheit.values())

    #Here we can confirm that the type of the data that we got back is a List Data Type.
print(type(fahrenheit.values()))

    #These Keys should be returned in the form of a List Object as well
print(fahrenheit.keys())
    
    #Here we can confirm that our keys are also being returned as a list object. 
print(type(fahrenheit.keys()))


#Mini Activity:
#We are going to create a function that will take in a temperature as a number representing the temperature in fahrenheit, and want to create a function that converts that to celsius.



#Solution using Functions 
'''

'''
def toCelsius(x):
    return float((5)/9) * (x-32)
'''

'''

#Solutions using Map and Lambda

    #This will create a list of celcius values from the fahrenheit values.
celsius = list(map(lambda x: (float(5)/9) * (x-32), fahrenheit.values()))

    #Print to confirm
#print(f"The values in celsius: {celsius}")


#Now that we have a new list of celsius values, and a set of keys from fahrenheit, we can "zip" together a new dictionary using lists and indicationg that one list will be of keys and the other of values. 
    #In this case I am taking my list of fahrenheit keys, and choosing to retain their values as keys, but am now zipping a new set of celsius values next to those temperature keys as opposed to the old fahrenheit values that were there.

#zip()
    #Packing together the keys from the list object representing the fahrenheit dictionary keys and the values from the celsius list object.
newDict = dict(zip(fahrenheit.keys(), celsius))
print(f"Final New Dictionary Product: {newDict}")
'''

'''
#Solution Using Dictionary Comprehension

fahrenheit2 = {"t1": 23, "t2": 56, "t3": 98, "t4": 0}

    #Just to confirm the items in the list. 
#print(fahrenheit2.items())

#Dictionary Comprehension To Generate a New Dictionary from an Old One. 
    #I will be using a dictionary with fahrenheit values and in one expression create a new dictionary with the same keys and new values. 
celsius = {k:((float(5)/9) * (v-32))for k,v in fahrenheit2.items()}

print(f"Dictionary Comprehension Version: {celsius}")
'''



#Review:
    #1. Mapping in Python
    #2. Filter in Python
    #3. Completed List Comprehension using Conditionals
    #4. Dictionary Comprehension 
    #5  Lambda Expression
    #6. Ternary Expression

#File Manipulation, File input and output. 
#python_object.python_method()

#There is probably some object that represents the file. 
#There is probablly some method that operates on that object. 












