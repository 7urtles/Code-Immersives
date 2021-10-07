
# -----[WORKING WITH FILES]-----
# Opening a file in x (exclusive) mode will create a file
# If the file already exists, an error will be received
# our_file = open('test_file.txt', 'x')
# Once done working with the file, close it to free up memory and usage of the file
# our_file.close()

# Accessing file contents is done using the open() function
our_file = open('test_file.txt')
# Once done working with the file, close it to free up memory and usage of the file
our_file.close()

# Before working with its contents, they should be stored to a variable
our_file = open('test_file.txt')

# There are four modes to open files with, r(EAD) w(RITE) a(PPEND) x(CLUSIVE)
#  Choose the appropriate one depending on what you want to do with the 
#   file, and place it's correspoding letter as the second argument of the open() function
our_file = open('test_file.txt', 'r')
for line in our_file:
    print(line)
# Once done working with the file, close it to free up memory and usage of the file
our_file.close()

# -----[READING]------
# Using read methods
our_file = open('test_file.txt')
# readline() returns a string containing text from one line in the file
one_line = our_file.readline()  # <= Reading one line
print(one_line)
our_file.close()

# Reading multiple lines with the readlines() method
our_file = open('test_file.txt')
# readlines() returns a list, each element in the list being a line from the file
list_of_lines = our_file.readlines()
print(list_of_lines)
our_file.close()


#-----[WRITING]-----
# After opening our file in w(RITE) mode
# The write() method is used to write data to a file.
# EXISTING DATA WILL BE OVERWRITTEN when you open a file in write mode 'w'
# If the file does not exist, it will be created.
new_file = open('test_file2.txt', 'w')
data = 'some data to be written to the file'
new_file.write(data)
# Close the file
new_file.close()


#-----[APPEND]-----
our_file = open('test_file2.txt', 'a')
our_file.write('\nAppending a line.')
our_file.close()


#-----[PROPERTIES]-----
# Open files have properties. 
# Some of these are name, mode, and encoding
#   Access properties through dot notation
our_file = open('test_file.txt')

print(our_file.encoding)
print(our_file.name)
print(our_file.mode)
our_file.close()

# You can position the cursor (point of operation) in an opened file 
#   with the .seek() method
# .seek() takes one argument (an index) as an integer which tells it where to put the cursor
#  within the file.

new_file = open('test_file2.txt', 'r+')
new_file.seek(5)
new_file.write('INJECTED')
new_file.close()

new_file = open('test_file2.txt', 'r')
lines = new_file.readlines()
print(lines)