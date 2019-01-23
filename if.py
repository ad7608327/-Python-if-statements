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
a = 6
b = 5
c = "5"
print("Your input was",a,b,c)
print("Your Input had string values let it to converted to integers",a,b,c)
#converting values into intgers
x = int(a)
y = int(b)
z = int(c)
print("\nAfter Converting the values into the integers",x,y,z)
#checking for equality between any two of them
def equal(x, y, z):
    if x==y or x==c or y==z:
        print("\nTrue")
        print("2 parameters are equal")
    else:
        print("\nFalse")
        print("None of the parameters are equal")

equal(x,y,z)


