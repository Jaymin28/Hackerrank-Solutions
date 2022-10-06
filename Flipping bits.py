# for result in decimal
def flippingBits(n):
    # Write your code here
    result = 0
    for i in range(31, -1, -1):
        if n // (2**i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += 2**i * x
    print(result)

flippingBits(9)

# for result in binary
def flippingBits(n):
    # Write your code here
    result = ''
    for i in range(31, -1, -1):
        if n // (2**i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += str(x)
    print(result)

flippingBits(9)

# for creating binary number in this code swap the value of x like x = 1 insted of x = 0 and do the same for other x