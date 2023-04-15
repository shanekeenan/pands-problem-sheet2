# squareroot.py 
# Task06 - week 6 
'''
Weekly task 6
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).
I suggest that you look at the newton method at estimating square roots.
This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.
'''
# author: Shane Keenan 
# status: ongoing 
# resources used: www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
'''
from resource: 
Newton’s Method: Let N be any number then the square root of N can be given by the formula: 
root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
In the above formula, X is any assumed square root of N and root is the correct square root of N.
'''
# input a floating point number 
floatnum = float(input('Please enter a floating point number:'))
# normal method 
squarefloat = floatnum ** .5 

tolerance = float(input('Please enter the tolerance required for the estimation: '))
# the fucntion sqrt() takes in two variables 
def sqrt(N,tolerance):
   estimate = 1.0
   while True:
        estimate = 0.5 * (estimate + (N / estimate)) 
        difference = abs(N - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate
print('\nYou entered this number: {} '.format(floatnum))
print('\nThe squareroot of {} is approximately equal to {:.5f} using x^0.5 method'.format(floatnum,squarefloat))
print('\nThe squareroot of {} is approximately equal to {:.5f} using newtons method with a tolerance of {}'.format(floatnum,sqrt(floatnum,tolerance),tolerance))