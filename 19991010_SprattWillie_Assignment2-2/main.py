# This program will calculate your age in the year of 2050
# Input: User Current Age, "myCurrentAge", Current Year, "currentYear"
# Output: Your current age and your future age in 2050

# INPUT function within an INT function that collects the current age of the user from placed in the "myCurrentAge" variable

myCurrentAge = int(input("What is your current age? \n"))

# INPUT function within an INT function that collects the current year from the user placed in the "currentYear" variable

currentYear = int(input("What is the current year? \n"))

# A variable called "myFutureAge" will hold a variable named "myCurrentAge"
# added to parenthesis holding the year 2050 with a subtraction of a variable
# called "currentYear" which holds the current year we are in.
myFutureAge = myCurrentAge + (2050 - currentYear)

# a PRINT functuin will be called telling the current age of the user

print("My current age is " + str(myCurrentAge))
# a PRINT function will be called telling the age the user will be in the year 2050

print("I will be " + str(myFutureAge) + " in 2050.")