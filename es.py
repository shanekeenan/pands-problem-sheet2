# es.py 
# Task 7 Week  7 
'''
Andrew's description: 
Write a program that reads in a text file and outputs the number of e's it contains. 
Think about what is being asked here, document any assumptions you are making.
The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
'''
# Author: Shane Keenan
# status: complete

# import the text file from an argument in the command line... 
# resource used : https://stackoverflow.com/questions/33766029/python-command-line-arguments-file-name
# https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ 
# moby dick text file 
# https://gist.github.com/StevenClontz/4445774 


# import the sys module 
import sys
# the sys.argv[1] gets the first argument after the script for a filename
filename = sys.argv[1]
#open the text file and read the contents 
with open(filename, 'r') as file:
    text = file.read()
#count the number of e's in the text file - i make the assumption that Andrew is requiring all e's in the text 
# both small e's and capital E's 
count = 0 
for char in text:
    if char == "e" or char =="E":
        count += 1
# count the number of lower case e's 
count_e = 0
for char in text:
    if char == "e" :
        count_e += 1
# count the number of upper case e's
count_E = 0
for char in text:
    if char == "E" :
        count_E += 1
print(f"\nAccording to the text file version of Moby Dick from https://gist.github.com/StevenClontz/4445774 \nThere is a total of {count} e's in the novel Moby Dick...",end = "")
print(f"{count_e} lower case e's and {count_E} upper case E's")