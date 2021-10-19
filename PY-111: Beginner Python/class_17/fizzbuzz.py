# print numbers between 1 and 100
# if number is divisible by 3 print 'fizz'
# if divisible by 5 print 'buzz'
# if divisible by both print 'fizzbuzz'
# if number is not divisible by any, print the number


[print("fizz"*(i%3==0)+"buzz"*(i%5==0) or i) for i in range(101)]