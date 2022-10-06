def maximumPerimeterTriangle(sticks):
    # Write your code here
    n = len(sticks)
    sticks = sorted(sticks)
    ans = (-1,-1,-1)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                a = sticks[i]
                b = sticks[j]
                c = sticks[k]
                if (a < b+c and b < a+c and c < a+b):
                    ans  = max(ans, (a,b,c))
    if ans[0] == -1:
        return (-1,'','')
    else :
        return ans