"""
Create a function that accepts 3 parameters and checks for equality between any two of them.
Your function should return True if 2 or more of the parameters are equal,
 and false is none of them are equal to any of the others.
"""
"""
Extra Credit:
Modify your function so that strings can be compared to integers if they are equivalent.
For example, if the following values are passed to your function:6,5,"5"

You should modify it so that it returns true instead of false.
Hint: there's a built in Python function called "int" that will help you convert strings to Integers.
"""
#Taking Values
a, b, c = int(input("Enter Number 1 > ")), int(input("Enter Number 2 > ")), input("Enter Number 3 > ")
print("<==========================================================>")
input("WARNING: We are sorry we stored your last number as string\nDont Worry We will Fix it ")
#converting values into intgers
c1 = int(c)
input("The Proplem Has been Fixed :)\nLet's Compare between your Numbers ")
#checking for equality between any two of them
def equal(a, b, c1):
    if a == b or b == c1 or c1 == a :
        input("\nTrue ")
        print("2 parameters are equal")
    else:
        print("\nFalse")
        print("None of the parameters are equal")
equal(a,b,c1)
