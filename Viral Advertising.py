def viralAdvertising(n):
    # Write your code here
    y = 5
    total = 0
    for i in range(n):
        x = int(y/2)
        total += x
        y = x*3
    return total