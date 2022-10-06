def funnyString(s):
    # Write your code here
    rev = s[::-1]
    n = len(s)
    i = 1
    x = y = list()
    for i in range(n):
        if (abs(ord(s[i-1]) - ord(s[i]))) != (abs(ord(rev[i-1]) - ord(rev[i]))):
            return 'Not Funny'
    return 'Funny'