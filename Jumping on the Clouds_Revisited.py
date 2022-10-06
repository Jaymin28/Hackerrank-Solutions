def jumpingOnClouds(c, k):
    i = 0
    e = 100
    n = len(c)
    while e == 100 or i:
        i = (i+k)%n
        e -= 1 + 2*(c[i])
    return e