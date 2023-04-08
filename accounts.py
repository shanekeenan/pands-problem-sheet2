# accounts.py 
# Task03 week3  

'''
 Description
# Write a python program called accounts.py
#   - that reads in a 10 character account number
#   - outputs the account number with only the last 4 digits showing
#   - (and the first 6 digits replaced with Xs).
'''

# Author: Shane Keenan 
# resources used:
# splcing -  https://www.pythonforbeginners.com/python-strings/string-splicing-in-python
# Status: complete 



#prompts user to enter a 10 digit account number assigned varible - account1 - input()- leave as a string of digits

account1 = input("Please enter a 10 digit account number:")

#  splice the account number to select the last 4 digits only  

last4_account1 = account1[6:10]

# print account number with first 6 digits replaced with x's 

print('\nxxxxxx{}'.format(last4_account1))





