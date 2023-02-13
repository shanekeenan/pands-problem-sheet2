# accounts.py 
# task03 week3  
# Description
# Write a python program called accounts.py
#   - that reads in a 10 character account number
#   - outputs the account number with only the last 4 digits showing
#   - (and the first 6 digits replaced with Xs).
# 
# https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths
# author: Shane Keenan 

# Status: ongoing 



#prompts user to enter a 10 digit account number assigned varible - account1 - input() defaults to a str so float() function converts to float

account1 = int(input("Please enter a 10 digit account number:"))

#check if the account number is 10 digits long   

elif len(account1) = 10:
    print "Error! Only 10 characters allowed!"
    sys.exit()




# prints the sum together with the euro symbol 
# checked stackoverflow again to format for 3 decimal places -  https://stackoverflow.com/questions/14540143/python-3-float-decimal-points-precision
# THis worked nicely - so even if you say.. add 120 and 150 it will display 2.70 instead of 2.7 


print('\nThe account number is xxxxxx {}'.format(account1))





