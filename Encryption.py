import math

def encryption(s):
    # Write your code here
    s.replace(' ','')
    L = len(s)
    sqr = math.sqrt(L)
    f = math.floor(sqr)
    c = math.ceil(sqr)
    result = []
    
    for i in range(c):
        temp = []
        j = 0
        while i + j < L:
            temp.append(s[i+j])
            j += c
        result.append(''.join(temp))
    
    return ' '.join(result)