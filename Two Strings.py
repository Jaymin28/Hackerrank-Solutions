def twoStrings(s1, s2):
    # Write your code here
    x = set(s1) & set(s2)
    if len(x) == 0:
        return 'NO'
    else :
        return 'YES'