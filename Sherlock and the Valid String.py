def isValid(s):
    # Write your code here
    from collections import Counter
    d = Counter(s)
    c = Counter(d.values())
    if len(c) == 1:
        return 'YES'
    elif len(c) > 2:
        return 'NO'
    else :
        minv = min(c.values())
        k1 , k2 = c.keys()
        if minv == 1:
            if min(k1, k2) == 1:
                if c[1] == 1:
                    return 'YES'
                else :
                    return 'NO'
            elif abs(k1-k2) == 1:
                return 'YES'
            else :
                return 'NO'
        else :
            return 'NO'