'''
Create a while loop that goes through the 12 days of 
Cristmas
    + on the 1 day of Christmas
    + on the 2 day of Christmas
    + ......12.................

Create a while loop that takes a list of integers and
returns the sum of them all
'''

def while_loop():
    counter = 1

    gift = [
    'A partridge in a pear tree',
    'Two turtle doves',
    'Three french hens',
    'Four calling birds',
    'Five gold rings',
    'Six geese a-laying',
    'Seven swans a-swimming',
    'Eight maids a-milking',
    'Nine ladies dancing',
    'Ten lords a-leaping',
    'Eleven pipers piping',
    'Twelve drummers drumming'
    ]

    while counter <= 12:
        line =f'On the {counter} of Christmas my true love game to me {gift[counter-1]}.'
        print(line)
        counter += 1
while_loop()