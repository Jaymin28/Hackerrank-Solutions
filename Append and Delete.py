def appendAndDelete(s, t, k):
    # Write your code here
    ls = len(s)
    lt = len(t)
    i = 0 
    while i < ls and i < lt and s[i] == t[i]:
        i += 1
    if k >= ls + lt:
        return 'Yes'
    elif k >= ls + lt - 2*i and (k - ls - lt + 2*i) % 2 == 0: 
        return 'Yes'
    else :
        return 'No'