def makingAnagrams(s1, s2):
    # Write your code here
    str1 = [0]*26
    str2 = [0]*26
    # 97 is the intial ascii value of lowercase alphabates
    for i in s1:
        ind = ord(i)-97
        str1[ind] += 1
    for j in s2:
        ind = ord(j)-97
        str2[ind] += 1
    
    total = 0
    for i in range(len(str1)):
        total += abs(str1[i] - str2[i])
    
    return total