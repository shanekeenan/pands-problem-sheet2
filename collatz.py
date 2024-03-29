# collatz.py 
# Task04 week4  
''' 
Description
# Write a python program called collatz.py
#   - that asks the user to input any positive integer and outputs the successive values of the following calculation.
#   - At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#   - Have the program end if the current value is one.
#   -  Push the program in your pands-problem-sheet GitHub repository (like you do for all the weekly tasks).
# Example of it running:
# Please enter a positive integer: 10
# 10 5 16 8 4 2 1
'''
# Author: Shane Keenan 
# Status: complete

#prompts user to enter any positive integer 
number_in = int(input("Please enter a positive integer:"))
# while the integer is not equal to 1 
# if() - the remainder of dividing by 2 is equal to 0 - it is an even number  - you divide by two 
# esle  - multipy by 3 and add 1 
# use print() of each iteration at the indentation level of the while loop. 
# the % operator changes a int into a float. - change to int to display neatly
# print('{} {}'.format(type(number_in),(number_in)))
# changed the sytnax of the print function from default end '\n' to end =' ' 
while (number_in != 1): 
    if (number_in % 2) == 0:
        number_in = (number_in/2)
    else:
        number_in = (number_in*3)+1
    print('{}'.format(int(number_in)),end= ' ')
    #print('{} {}'.format(type(number_in),(number_in)))