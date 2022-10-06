def getMinimumCost(k, c):
    c.sort(reverse = True)
    ans = 0
    count = 0
    for el in c:
        ans += (el * (1 + (count//k)))
        count += 1
    
    return ans