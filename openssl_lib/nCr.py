def binomialCoeff(n , k):

    if k==0 or k ==n :
        return 1

    # Recursive Call
    return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k)

# Driver Program to test ht above function
n = 5
k = 2
print "Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k))

# output: Value of C(5,2) is 10
