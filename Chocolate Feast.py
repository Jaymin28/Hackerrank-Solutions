def chocolateFeast(n, c, m):
    # Write your code here
    x = n//c
    ch = x
    w = x
    while w//m > 0:
        nch = w // m
        ch += nch
        w = (w % m) +  nch
    return ch