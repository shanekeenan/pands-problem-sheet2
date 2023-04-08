# accounts_extra.py 
# Task03 week3  

'''
Description
# Write a python program called accounts.py
#   - that reads in a 10 character account number
#   - outputs the account number with only the last 4 digits showing
#   - (and the first 6 digits replaced with Xs).
# Extra:
# Modify the program to deal with account numbers of any length
# (yes that is a vague requirement, comment your assumptions)

'''

# author: Shane Keenan 

# resources used:
#splcing -  https://www.pythonforbeginners.com/python-strings/string-splicing-in-python
# generate a string of x's https://stackoverflow.com/questions/1424005/in-python-how-do-i-create-a-string-of-n-characters-in-one-line-of-code
# determine the length of a string  - https://www.w3schools.com/python/gloss_python_string_length.asp 

# Status: complete


#prompts user to enter  account number of any length assigned varible - account1 - input()- leave as a string of digits

account1 = input("Please enter account number of any length:")

#  check what length the account number is 

length_account1 = len(account1)

# just to check what type of variable the function len() gives
length_type = type(length_account1)
#print('{}'.format(type(length_account1)))

#  splice the account number to select the last 4 digits only   
last4_account1 = account1[length_account1-4:length_account1]

# print account number with first 6 digits replaced with x's 
print('The account number is {} digits long'.format(length_account1))

#generates a string of x's the length of the account number minus the last 4 digits 
string_x = "x" * (length_account1-4)


print('\n{}{}'.format(string_x,last4_account1))





