def theLoveLetterMystery(s):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rev = s[::-1]
    ans = 0
    for i in range(len(s)//2):
        x = s[i]
        y = rev[i]
        pos1 = alphabet.find(x)
        pos2 = alphabet.find(y)
        ans += abs(pos2-pos1)
    return ans