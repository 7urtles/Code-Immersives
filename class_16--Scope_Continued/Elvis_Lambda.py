#We are used to writing functions in this class... We have worked with simple ones like adding numbers and performing other arithmetic, to operating on lists and extracting information from processing the data. 

#Well here is another one of those handy Python features that came out 3.4+ and it's one of those that can turn creating a function to a one-liner.... But remember that these one-liners come at a price. There is so much happening behind the scenes, that to the naked eye it'll look like that little bit of code can't possibly be doing this much there has to be something more, and really it's that one line of code is so dense with fundamentals that one line is all that is required and developers are always working and striving to make these programming langauges easier to use. 

#Alright, let's talk about expressions, because that is what lambda is, an expression. 

#Expressions are one liners, that evaluate to some value or data type, and those data types as opposed to statements can be stored in a variable, or passed into an argument as if it were a simple variable. 

x = "Hello World" #My expression here is a String, the String Hello World. Simple. This is what we are used to. 

#Here is another example of a one-liner in action. This will turn your if and else statements into an expression, which means that you'll be able to store their values or pass them in as arguments.

''' 
userInput = int(input("How old are you, please enter a number: "))
canDrink = "You Good..." if userInput > 21 else "You got to go...."
print(canDrink)
print(type(canDrink))

'''

#Do a little bit of practice with this. Go ahead and recreate some conditional logic from previous activities using the ternary operator syntax in Python
#Understand, it will never read more English than that.


'''
Lambdas are one line functions. They are also known as anonymous functions in some other languages. You might want to use lambdas when you don’t want to use a function twice in a program. They are just like normal functions and even behave like them.
'''
#If we wanted to add numbers the tradional way we would use:

''' 
def add(x, y):
    return x + y
'''

#That's not so bad, but that's not a one liner. Also, I can't necessary store that value as a variable since it isn't an expression, I can call it as a function since that is what it is. 

#Notice that this particular function is a one-liner function. It only does one thing directly from within the arguments passed in. Those are the functions that are translatable to Lambda. That is because the lamdba expression can only take one expression as a value and that is what you would like to return. 

#Now let's say that we wanted to: 
    #Only return True if the numbers added up are over 42, or return False otherwise.

'''

def specialAdd(x, y):
    if((x + y) > 21):
        return True
    else: 
        return False

'''

#All of a sudden the logic gets more complex. That's normal, since you're adding conditional logic to your functionality. 


#Let's go ahead and turn those Functions and Conditionals from Statements to Expressions using Ternary and Lambda and try to acheive the same result. 


#The way that you interpret Lambda functions are as follows: 

#lamdba argument(s): expression

#Here is an example:

'''

add = lambda x,y : x + y 
print(add(3, 4))

'''

#Now that we have that out of the way, we can also use a ternary expression to evaluate the result we want out of our lambda function. For example like the one above. 

'''

specialAdd = lambda x,y: "You both good..." if (x + y) > 21 else "You both got to go..."

print(specialAdd(23, 13))

'''

#That will conclude our lesson on Lambda. 

#I will be coming up with Activities for this particular topic, and what follows this will be Map, Filter, and Reduce. You will see Lambda Expressions be especially useful there. 
