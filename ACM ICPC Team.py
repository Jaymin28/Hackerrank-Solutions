def acmTeam(topic):
    # Write your code here
    maxm = 0
    cnt = 0
    l = list()
    n = len(topic)
    m = len(topic[0])
    for i in range(n-1):
        for j in range(i+1,n):
            count = bin(int(topic[i],2) | int(topic[j],2)).count('1')
            if count > maxm:
                maxm = count
                cnt = 1
            elif count == maxm:
                cnt += 1
    return (maxm, cnt)

"""
    here  "bin(int(topic[i],2) | int(topic[j],2))"
    bin() convert any int to binery string

    and  "int(topic[i],2)"
    convert any binery string to integer
    here 2 means given string is binary string
    if given value is hexcode then we have to write 6
    and for Hexadecimal we have to write 16

    and a | b 
    this is called or operation
    or operation can be done between two integers
    and it returns or of their binery values

"""