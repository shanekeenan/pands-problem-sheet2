# pands-problem-sheet   

<h1>README file for weekly tasks in the Programming and scripting module semester 1 HDip in Computing in Data Analytics</h1>


<h1>Task01 from Week 1</h1>
 <h2> Task description </h2> 


- Please simply introduce yourself in the Discussion forum, 
- Install the required software on your machine,
- Pull the sample code in my repository to your machine,
- Create a GitHub account and repository for yourself (mywork), and the problem sheet (pands-problem-sheet)
- Commit and push a file to the problem sheet called helloworld.py. This file should contain a python program that displays Hello World! when it is run.


<h2> Key learnings and structure </h2>

use of the print() function to output/display text to user 


status: <i>complete</i>


<h1>Task02 from week 2 </h1>
 <h2> Task description </h2> 
 
The program should:
 The program should:
  - Prompt the user and read in two money amounts (in cent)
   - Add the two amounts
   - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 


<h2> Program:  </h2>

bank.py

<h2> Key learnings and structure </h2>

prompting for a user input - and converting that string to a float 

amount1 = float(input("Please enter an amount of money in cent:"))

<h2> Resources/ references </h2>

stackoverflow on how to get the euro symbol: code from here https://stackoverflow.com/questions/39935857

status: <i>complete</i>

<h1>Task03 from week 3 </h1>
 <h2> Task description </h2> 
 
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
Extra:
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)


<h2> Key learnings and structure </h2>


prompting for a user input - and converting that string to a float 

amount1 = float(input("Please enter an amount of money in cent:"))


status: <i>complete</i>

<h1>Task04 from week 4 </h1>
<h2> Task description </h2> 

Description:
Write a python program called collatz.py
   - that asks the user to input any positive integer and outputs the successive values of the following calculation.
   - At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
   - Have the program end if the current value is one.
   -  Push the program in your pands-problem-sheet GitHub repository (like you do for all the weekly tasks).
 Example of it running:

 Please enter a positive integer: 10
 10 5 16 8 4 2 1


<h2> Key learnings and structure </h2>

Great task to get to grips with both while loops and if/else statements 

Solution:

#prompts user to enter any positive integer 
number_in = int(input("Please enter a positive integer:"))

# while the integer is not equal to 1 
# if() - the remainder of dividing by 2 is equal to 0 - it is an even number  - you divide by two 
# esle  - multipy by 3 and add 1 
# use print() of each iteration at the indentation level of the while loop. 
# noticed that using the % operator changes a int into a float. - need to change to int to display neatly

print('{} {}'.format(type(number_in),(number_in)))

while (number_in != 1): 
    if (number_in % 2) == 0:
        number_in = (number_in/2)
    else:
        number_in = (number_in*3)+1
    print('{}'.format(int(number_in)))
    #print('{} {}'.format(type(number_in),(number_in)))



status: <i>complete</i>


h1>Task05 from week 5 </h1>
 <h2> Task description </h2> 
 
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.

An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!


<h2> Key learnings and structure </h2>


import datetime
weekday_no = datetime.datetime.today().weekday()

this returns an integer 0-6 representing the consecutive days of the week, starting from Monday.


User an if/else statement to output text depending on whether it is a weekday or the weekend 

if weekday_no < 5:
    print ("Yes, unfortunately today is a weekday.")
else:  # 5 Sat, 6 Sun
    print ("It is the weekend, yay!")


An addition to the program to output the day as well - to make a list of the weekdays and use the weekday_no integer to select the correct index in the list 

days = ['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday', 'Sunday']
print(f"It's " +days[weekday_no] )




status: <i>complete</i>



<h1>Task06 from week 6 </h1>
<h2> Task description </h2> 

Description:


<h2> Key learnings and structure </h2>





status: <i>complete</i>


<h1>Task07 from week 7 </h1>
<h2> Task description </h2> 

Description:


<h2> Key learnings and structure </h2>





status: <i>complete</i>



<h1>Task08 from week 8 </h1>
<h2> Task description </h2> 

Description:


<h2> Key learnings and structure </h2>





status: <i>complete</i>
