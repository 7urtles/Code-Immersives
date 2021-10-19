# -----[SLICES]-----
'''
Slices are used to get a portion, or 'slice', of a string or other iterable object
The syntax of using a slice is 3  integer arguments seperated by a colon ':' with brackets '[]' as such:
      [1:1:1]

The meanings of the three positions are:
1. The starting point
2. The ending point (not including this position)
3. The step count (how many positions to increase by)
'''
# Getting the first three letter of a word is done like so:
word = 'slicing'
word = word[0:3:1]
print(word)

# Getting every other letter:
word = 'abcdefghijklmnop'
word = word[0:-1:2]
print(word)

'''
Additionally you may leave an argument out of calling a slice if its
default is intended.

These are the defaults per position:
    1. The begenning
    2. Then end
    3. A step count of 1
'''

# Example:

word = 'abcdefghijklmnop'
word = word[::2]
print(word)
