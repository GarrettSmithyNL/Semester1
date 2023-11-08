# This is the program to try and expirement with strings
# Garrett Smiht
# Oct 10

# Constants
FIRST_LETTER = 0
SPACE = " "

# Gathering Inputs
title = input("Your title: ").capitalize()
firstName = input("Enter your first name: ").capitalize()
lastName = input("Enter your last name: ").title()

# Processing
firstLetter = firstName[FIRST_LETTER] + "."

if title.endswith(".") == False:
    title += "."

output1 = title + SPACE + firstName + SPACE + lastName
output2 = firstLetter + SPACE + lastName
output3 = title + SPACE + firstLetter + SPACE + lastName
output4 = lastName + ", " + firstName
output5 = lastName + ", " + firstLetter

# Output
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
