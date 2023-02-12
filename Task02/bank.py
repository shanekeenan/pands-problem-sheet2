# bank.py 
# task02  
# Description
# The program should:
#   - Prompt the user and read in two money amounts (in cent)
#   - Add the two amounts
#   - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# 
# i searcherd stackoverflow on how to get the euro symbol: code from here https://stackoverflow.com/questions/39935857


# author: Shane Keenan 

# Status: complete

import unicodedata

#prompts user to enter an amount in cents assigned varible - amount1 - input() defaults to a str so float() function converts to float

print('This program will add two amounts of money togther in cents and display in Euro \n')

amount1 = float(input("Please enter an amount of money in cent:"))

#prompts user to enter a second amount in cents assigned varible - amount2 

amount2 = float(input("Please enter a second amount of money in cent:"))

# add the two amounts together 

sum = (amount1 + amount2)/100 

# i wanted to display the sum amount with 3 significant figures even when there is no single cents - 
# I thought this round() might do it but it didn't 
sum_round = round(sum,3)

# prints the sum together with the euro symbol 
# checked stackoverflow again to format for 3 decimal places -  https://stackoverflow.com/questions/14540143/python-3-float-decimal-points-precision
# THis worked nicely - so even if you say.. add 120 and 150 it will display 2.70 instead of 2.7 


print('The sum of these two amounts is {}{:.2f} '.format(unicodedata.lookup("EURO SIGN"), sum_round))





