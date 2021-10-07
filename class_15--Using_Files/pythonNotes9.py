#Introductions: 
#A file is an object on a computer that stores data, information, settings, and/or commands used with a computer program

#All Object have: 
#1. Property/Type  -> "Elvis", [1, 2, 3, 4]
#2. Behavior/Methods -> .append(), .max(), .count(), keys(), values(), items(), .sort(), sorted(), list(), dict(), tuple(), map(), zip()


#An example of a computer program would be your Python File/Module. 

#What are some advantages of files: 
# 1. Data is stored permanently 
# 2. Updating can be made easy
# 3. Data can be shared among various programs that also work with file objects 
# 4. Huge amounts of data that can be stored in a file

#I want you to know that in general there are two types of files: 
# 1. Text File
# 2. Binary File

#In this lesson and this course, we will be focusing on Text Files: 

#Text Files store the data in the form of "Strings":

#Example: 
'''

"Ram" -> That is stored as 3 characters
234.98 -> That is stored as 6 characters
"   " -> That is 3 characters
'''

#Then there are examples of text files such as: .txt, .c, or .cpp. 
#In today's class we are working with text files with the ".txt" extension

#Let's begin talking about what Python can do with files. Starting with OPENING one: 

#Python has a built in method called "open()"

#Example: 
'''

myFile = open(<file_name>, <open_mode>)

'''

#Our immidiate next questions should be: 
'''
#Student Questions: 
#1. Whatchu mean by <open_mode>
#2. Can You use Path for File Name?
#3. In what context would you use this?
#4. Can you open multi files with that one line?
'''

#Elvis's Pre-Defined Questions: 
'''
#1. What is <open_mode>?
#2. What is <file_name> referring to
#3. Are those two "<file_name> <open_mode>" parameter?
#4. Open is a method?
#5. myFile is the variable storing the newly opened file object?
'''

#Elvis's Pre-Defined Answers: 
'''
#1. myFile indeed is the variable name, and it is assigned the value of the open method with two parameters of "<file_name> <open_mode>"
#2. open() indeed is a method that is used to open a file in Python, and it takes in at least two arguments as referenced above with "<file_name> <open_mode>"
#3. <file_name> and <open_mode> are the parameters that you substitute with arguments representing what those paramters are expecting
#4. <file_name> is referring to the name you want your file to have. Similar to when we hit "Command+S". We choose a name and an extension. Except we are not using our Computer's Graphic User Interface or OS (Operating System) to accomplish this. We are using pure python. 
#5. <open_mode> is referring to a character code that grants different privelages to the file that you are currently creating. The different <open_mode>'s are: 
    #5.1: "w" -> To write the data. If the file already exists, the data will be overwritte.
    #5.2: "r" -> To read the data. The file pointer is positioned at the beginning of the file
    #5.3: "a" -> To append data to a file. The file pointer is positioned at end of the file. 
    #5.4: "w+" -> To write AND read data to/from a file. If the file already exists, the previous data will be overwritten (or lost...)
    #5.5: "r+" -> To read AND write data from/to a file. If the file already exists, your previous data will not be deleted. The file is placed in the beginning of the file. 
    #5.6: "a+" -> To append and to read data from a file. The file pointer will be at the end of the file. 
    #5.7: "x" -> To open the file in exclusive creation mode. the file creation will FAIL if the file already exists. Meaning this is simply to create the file. 
'''

#Let's do an example of each and test them to see their results: 
    #The "x" mode will purely create a file with the specified name. 
    #If the file already exists, you will be retuning a "FileExistsError" indicating that the file exists already and therefore you cannot recreate it. 
#myFile = open("Silver5.txt", "x")

#Now that I have created the "Silver5.txt" file and you see it open up in my local directory. Let's add some information into it. 

#The "r" mode will read from an existing file in an existing path. If it does exist, then it will allow us to "read" from that file. That means that we can use a set of "read" methods namely ".read()" and ".readline()" and ".readlines()" that will allow us to read from the file. 
    #This is also the "default" value for the "mode" argument with your "open()" method. This means, if you don't indicate a mode, it'll be "r". 
#myFile3 = open("Elvis1.txt", "r")

#The read() method will return to you a String Object with the content of the entire file. 
#entireFile = myFile3.read()

#The readline() method will return to your a String Object with the current line where the pointer is in the file. If you call it the first time, then the pointer will be on the second line. 
# firstLine = myFile3.readline()

#When you call the readline() method a second time, since you never closed the file or anything, your pointer is currently in the beginning of the second line. Therefore, it will record the content of the second line as a String Object this time around. 
# secondLine = myFile3.readline()

#This pattern will repeat for as many lines as there are in your file. 
# thirdLine = myFile3.readline()

#The readlines() method will return a list of all the lines as list items including the special character for newline escape sequence \n. 
#lines = myFile3.readlines()


#print(entireFile)
# print(firstLine)
# print(secondLine)
# print(thirdLine)
#print(lines)
#print(type(lines))

#myFile3.close()















#myFile2 = open("Elvis1.txt", "w")
# myFile2.write("Hello World!")

#If I were to write again to my file, what will happen is that the "pointer" will be at the front of the file, and then will overwrite any data in the file with the data that we put in the last "write()" method.

#myFile2.write("Elvis is the Greatest of All Time")

#File Objects have Properties. If you were to try to print the file object accidentally in order to read its contents, you will instead receive a reference to the object and its properties.
#print(myFile2) 

#You can refer to those properties like this: 
# print(myFile2.name)
# print(myFile2.mode)
# print(myFile2.closed)

#Make sure that you close your file when finished with your operations. This will save resources on your computer from dedicating to the file your app is creating. 
#myFile2.close()


#Now let's say that we would like to write to the END of a file. That's where the "a" append mode comes in handy. That will put your pointer at the very end of the file. This makes it so that anything that you write into the file is appended to the end of the file. 

'''
myFile4 = open("Elvis1.txt", "a")
myFile4.write("\nis the greatest of all time!\n")
'''









#This "r+" allows you to refer to a file that already exists. It also let's you write to that file. 
    #It will not overwrite any of the information in that file. 
    #It will add the String you're adding to the file at the top of the file if you haven't read from the file or at the bottom of the file if you have read from the file. 
    #That is because remember, if you have not read yet, the pointer is at the beginning of the file
    #If you do read the pointer is at the end that is why it takes this behavior. 
'''
myFile5 = open("Elvis1.txt", "r+")
myFile5.write("What's up, it's me, File Number 5. Just here doing my thing at the top\n")
entireFile = myFile5.read()
myFile5.write("What's up, it's me, File Number 5. Just here doing my thing at the bottom\n")
print(entireFile)
'''

'''
myFile6 = open("Elvis2.txt", "a+")
myFile6.write("\nSome new Information on this new line.")
print(myFile6.readlines())
'''



