def superReducedString(s):
    # Write your code here
    if len(s) == 1:
        return s
    i = 1
    while i < len(s):
        if s[i] == s[i-1]:
            if len(s) == 2:
                return 'Empty String'
            s = s[:i-1] + s[i+1:]
            i = 1
        else :
            i += 1
    
    if len(s) == 0:
        return 'Empty String'
    else :
        return print(s)

# example
superReducedString('aaabccd')