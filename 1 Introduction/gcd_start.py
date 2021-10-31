# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    while (b != 0):
        t= a        #20 - 8
        a = b       #8  - 4
        b = t % b   #2 and reminder is 4   - 1 and reminder is 0

    return a


        
# try out the function with a few examples
print(gcd(10, 5))  # should be 12
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
