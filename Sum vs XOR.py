def sumXor(n):
    # Write your code here
    result = 1
    while n:
        b = n&1
        n >>= 1
        if b == 0:
            result *= 2
    return result