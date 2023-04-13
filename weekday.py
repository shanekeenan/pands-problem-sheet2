# weekday.py 
# task05 week5  


'''
Description from Andrew 
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
(You will need to search the web to find how you work out what day it is)
An example of running this program on a Thursday is given below.
$ python weekday.py
Yes, unfortunately today is a weekday.
An example of running it on a Saturday is as follows:
$ python weekday.py
It is the weekend, yay!

'''
# Author: Shane Keenan
# resource used: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# status: complete

import datetime
weekday_no = datetime.datetime.today().weekday()
# sanity check 
'''
print(type(weekday_no)) 
print(weekday_no)
'''
# test the if/esle statement 
# weekday_no = 6
if weekday_no <= 5:
    print ("Yes, unfortunately today is a weekday.")
else:  # 5 Sat, 6 Sun
    print ("It is the weekend, yay!")
# addition to the program is to make a list of the weekdays and use the weekday_no integer to select the correct index in the list 
days = ['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday', 'Sunday']
print(f"It's " +days[weekday_no] )



