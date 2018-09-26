# Python program to find LCM of two numbers

# Recursive function to return gcd of a and b
def gcd(a,b):

    # base case if a and b are equal
    if (a == b):
        return a
    # if a is greater
    if (a > b):
        return gcd(a-b, b)

    return gcd(a, b-a)

# Function to return LCM of two numbers
def lcm(a,b):
    return (a*b) / gcd(a,b)

# Driver program to test above function
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))

# output: LCM of 15 and 20 is 60
