def anagram(s):
    # Write your code here
    num = 0
    n = len(s)
    if n % 2 != 0:\
        return -1
    else : 
        mid = int(n/2)
        s1 = s[:mid]
        s2 = list(s[mid:])
        for i in range(len(s1)):
            try:
                s2.remove(s1[i])
            except:
                num += 1
    return num