def maximizingXor(l, r):
    # Write your code here
    maxx = 0
    for i in range(l,r+1):
        for j in range(i,r+1):
            maxx = max(maxx, i^j)
    return maxx