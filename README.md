# pands-problem-sheet   

<h2>README file for weekly tasks in the Programming and scripting module semester 1 HDip in Computing in Data Analytics</h2>
Author: Shane Keenan

This README file contains the description of my programs/solutions for the weekly tasks 1-8 in this module.<br>
Included are descriptions of the following programs:<br>
    <li> <i>helloworld.py (task01)</i></li>
    <li> <i>bank.py (task02)</i></li> 
    <li> <i>account.py and account_extra.py(task03)</i> </li>
    <li> <i>collatz.py (task04)</i></li>
    <li> <i>weekday.py (task05)</i></li>
    <li> <i>sqaureroot.py (task06)</i></li>
    <li> <i>es.py (task07)</i></li>
    <li> <i>plottask.py (task08)</i></li>

All of the programs listed above were developed with and for use with Visual Studio Code. 
<h2>Task01 from Week 1</h2>
 <h3> Task description </h3> 
- Please simply introduce yourself in the Discussion forum, 
- Install the required software on your machine,
- Pull the sample code in my repository to your machine,
- Create a GitHub account and repository for yourself (mywork), and the problem sheet (pands-problem-sheet)
- Commit and push a file to the problem sheet called helloworld.py. This file should contain a python program that displays Hello World! when it is run.
<h3> Program:  </h3>
helloworld.py
<h3> Key learnings and structure </h3>
use of the print() function to output/display text to user 
<h3>status: </h3>
<b><i>complete</i></b>





<h2>Task02 from week 2 </h2>
 <h3> Task description: </h3> 
    - Prompt the user and read in two money amounts (in cent)<br>
   - Add the two amounts<br>
   - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount<br> 
<h3> Program:  </h3>
<i>bank.py</i>
<h3> Key learnings and structure:</h3>
prompting for a user input - amount1 = float(input("Please enter an amount of money in cent:"))<br>
dividing two integers (/100) will convert to a float anyway so easiest to convert that string directly to a float<br>
used formatting to display 3 significant figures<br>
print('\nThe sum of these two amounts is {}{:.2f} '.format(unicodedata.lookup("EURO SIGN"), sum_round))
<h3> Resources/ references </h3>
stackoverflow on how to get the euro symbol: code from here https://stackoverflow.com/questions/39935857
<h3>status: </h3>
<b><i>complete</i></b>




<h2>Task03 from week 3 </h2>
 <h3> Task description: </h3>  
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).<br>
Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).<br>

python accounts.py  <br>
Please enter an 10 digit account number: 1234567890<br>
XXXXXX7890<br>
Extra:<br>
Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

<h3> Program:  </h3>
<i>account.py and account_extra.py</i>
<h3>Key learnings and structure: </h3>
prompts the user for a 10 digit account number - user input - variable string<br>
because it is 10 digits long the account number can be spliced using a simple<br>
last4_account1 = account1[6:10]<br>
and displayed showing the only the last 4 digits<br>
print('\nxxxxxx{}'.format(last4_account1))

account_extra.py <br>
this one deals with the case of an account number of unknown length<br> 
and uses splicing with a negative number to select the last 4 digits.<br>
last4_account1 = account1[-4:]<br>
the len() function is used to determine the length of the account number and the number of x's to include when displayed. 


<h3> Resources/ references: </h3>
splcing -  https://www.pythonforbeginners.com/python-strings/string-splicing-in-python
generate a string of x's https://stackoverflow.com/questions/1424005/in-python-how-do-i-create-a-string-of-n-characters-in-one-line-of-code
determine the length of a string  - https://www.w3schools.com/python/gloss_python_string_length.asp 

<h3>status: </h3>
<b><i>complete</i></b>








<h2>Task04 from week 4 </h2>
 <h3> Task description: </h3>  
Write a python program <br>
   - that asks the user to input any positive integer and outputs the successive values of the following calculation.<br>
   - At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.<br>
   - Have the program end if the current value is one.<br>
   -  Push the program in your pands-problem-sheet GitHub repository (like you do for all the weekly tasks).<br>
 Example of it running:<br>

 Please enter a positive integer: 10<br>
 10 5 16 8 4 2 1<br>

<h3> Program:  </h3>
<i>collatz.py</i>
<h3>Key learnings and structure: </h3>

use while loop for the integer is not equal to 1<br> 
if statement - the remainder of dividing by 2 is equal to 0 - it is an even number  - you divide by two <br>
esle  - multipy by 3 and add 1<br> 
use print() of each iteration at the indentation level of the while loop.<br> 
note using the % operator changes a int into a float. - change to int inside print()<br>
to avoid printing each number on a new line change the syntax of the print() fucntion to use a space instead.  <br>
print('{}'.format(int(number_in)),end= ' ')

<h3> Resources/ references: </h3>



<h3>status: </h3>
<b><i>complete</i></b>








<h2>Task05 from week 5 </h2>
 <h3> Task description: </h3>  
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)<br>
(You will need to search the web to find how you work out what day it is)<br>
An example of running this program on a Thursday is given below.<br>

$ python weekday.py
Yes, unfortunately today is a weekday.
An example of running it on a Saturday is as follows:
$ python weekday.py
It is the weekend, yay!

<h3> Program:  </h3>
<i>weekday.py</i>

<h3>Key learnings and structure: </h3>

import datetime<br>
weekday_no = datetime.datetime.today().weekday()<br>
if/else statement checks if the variable "weekday_no" is less than 5 -  0-6 is Mon-Sun.<br>
addition to the program is to make a list of the weekdays and use the weekday_no integer to select the correct index in the list 

<h3> Resources/ references: </h3>
stackoverflow on how to get the euro symbol: code from here https://stackoverflow.com/questions/39935857

<h3>status: </h3>
<b><i>complete</i></b>





<h2>Task06 from week 6 </h2>
 <h3> Task description: </h3>  
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.<br>
You should create a function called <t>sqrt</t> that does this.<br>
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).<br>
This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).<br>
I suggest that you look at the newton method at estimating square roots.<br>
This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

<h3> Program:  </h3>
<i>squareroot.py</i>

<h3>Key learnings and structure: </h3>

geeksforgeeks.org described Newton's method.. <br>
"Newton’s Method: Let N be any number then the square root of N can be given by the formula:<br>
root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.<br>
In the above formula, X is any assumed square root of N and root is the correct square root of N."<br>

the fucntion sqrt() takes in two variables - the number to solve for the sqaureroot and the tolerance which is used to determine when to break the while loop. We start with the estimate = 1 (X =1). 

the estimated squareroot is compared with N^0.5. 

<h3> Resources/ references: </h3>
resources used: www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

<h3>status: </h3>
<b><i>complete</i></b>





<h2>Task07 from week 7 </h2>
 <h3> Task description: </h3>  
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.<br>
The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
<h3> Program:  </h3>
<i>es.py</i>

<h3>Key learnings and structure: </h3>
import the sys module <br>
import sys
<br>
the sys.argv[1] gets the first argument after the script for a filename<br>
filename = sys.argv[1]
<br>
count the number of e's in the text file - i make the assumption that Andrew is requiring all e's in the text 
both small e's and capital E's 
<br>
the program uses for loops to count the total nubmer of e characters, individual lower case e's and upper case E's. 

<h3> Resources/ references: </h3>
how to import the text file from an argument in the command line - 
https://stackoverflow.com/questions/33766029/python-command-line-arguments-file-name
https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ 
moby dick text file -  https://gist.github.com/StevenClontz/4445774 

<h3>status: </h3>
<b><i>complete</i></b>




<h2>Task08 from week 8 </h2>
 <h3> Task description: </h3>  
Write a program called plottask.py that displays:<br>
a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.<br>
Some marks will be given for making the plot look nice (legend etc).
<h3> Program:  </h3>
<i>plottask.py</i>
<h3>Key learnings and structure: </h3>
program uses numpy to generate the data required for the histogram and function.<br>

program uses object-orientated matplotlib for the plotting. <br>

program saves plot as hist_func_plot.png - plt.savefig('hist_func_plot.png')

<h3> Resources/ references: </h3>
https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/
https://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o
https://www.geeksforgeeks.org/matplotlib-pyplot-twinx-in-python/
https://stackoverflow.com/questions/21226868/superscript-in-python-plots

<h3>status: </h3>
<b><i>complete</i></b>














<h1>Task04 from week 4 </h1>
<h2> Task description </h2> 

Description:



<h2> Key learnings and structure </h2>

Great task to get to grips with both while loops and if/else statements 






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
