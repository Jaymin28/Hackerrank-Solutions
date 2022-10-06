def jumpingOnClouds(c):
    # Write your code here
    i = 0
    count = 0
    while i < len(c)-2:
        if c[i+2] == 0:
            i += 2
        else :
            i += 1
        count += 1
    if i != len(c)-1:
        count += 1
    return count