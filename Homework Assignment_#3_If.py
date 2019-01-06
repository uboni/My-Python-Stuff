'''
Following function checks for equality between any two of inputs that as passed
This is part Assignment #3
Checks for the equality of any of 2 inputs that are passed 
'''
def checkEquality(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)

    if (a == b) or (b == c) or (c == a) or (a == b ==c):
        return True
    elif (a != b and b != c and a != c):
        return False
print(checkEquality(1,2,"3"))
print(checkEquality(1,1,"3"))
print(checkEquality(1,1,"1"))
