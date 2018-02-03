"""
Program:		ATM
Author:			Randall Rowland
Class:			IT-140-Q3788 Introduction to Scripting 18EW3
Instructor:		Angel D. Cross
Date:			1 Feb 2018
Description:    The task for this project is to create a very simple ATM that addresses
                developing functions and using regular expressions to search for patterns.
Repository:     https://git.io/vNA9t
Input:          stdin
Output:         stdout
Known bugs/missing features:


Modifications:
Date                Comment
----    ------------------------------------------------
"""
import sys

# account balance
account_balance = float(500.25)


# <--------functions go here-------------------->
# Rubric inject: print balance function
def balance():
  print("Your current balance:\n" + str(account_balance)) # Rubric inject: example of functions that return the correct output


# Rubric inject: deposit function
def deposit():
    global account_balance
    depositAmount = raw_input("How much would you like to deposit today?\n") # Rubric inject: input (parameters) that are utilized within the function(s)
    account_balance += float(depositAmount)
    print("Deposit was $" + str('%.2f' % float(depositAmount)) + ", current balance is $" + str(account_balance)) # Rubric inject: example of functions that return the correct output


# Rubric inject: withdraw function
def withdraw():
    global account_balance
    withdrawAmount = raw_input("How much would you like to withdraw today?\n") # Rubric inject: input (parameters) that are utilized within the function(s)
    if float(withdrawAmount) > account_balance:
        # Rubric inject: example of functions that return the correct output
        print("$" + str('%.2f' % float(withdrawAmount)) + " is greater that your account balance of $" + str('%.2f' % float(account_balance)))
    else:
        account_balance -= float(withdrawAmount)
        # Rubric inject: example of functions that return the correct output
        print("Withdrawal amount was $" + str('%.2f' % float(withdrawAmount)) + ", current balance is $" + str('%.2f' % float(account_balance)))


# Rubric inject: quit function
def quit():
    print("Thank you for banking with us.") # Rubric inject: example of functions that return the correct output


# User Input goes here, use if/else conditional statement to call function based on user input

userchoice = raw_input("What would you like to do?\n")

options = {'B': balance,
           'W': withdraw,
           'D': deposit,
           'Q': quit,
}

options[userchoice]()
# Used to determine which function to run instead of using several if statements
