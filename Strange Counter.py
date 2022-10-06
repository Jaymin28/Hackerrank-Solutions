def strangeCounter(t):
    # Write your code here
    n = 3
    while (2*n - 2) <= t:
        n *= 2
    ans = n - (t-(n-2))
    return int(ans)