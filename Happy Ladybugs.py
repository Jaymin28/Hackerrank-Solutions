def happyLadybugs(b):
    # Write your code here
    from collections import Counter
    from itertools import groupby
    c = Counter(b)
    if "_" in c:
        for x,y in c.items():
            if y<2 and x!="_":
                return "NO"
    else:
        for x,y in groupby(b):
            if len(list(y))<2:
                return "NO"
    return "YES"

'''
# explanation of groupby()

import itertools
a = "aaabbbccccd"
x = itertools.groupby(a)
for k,g in x:
    print(k, list(g))

'''