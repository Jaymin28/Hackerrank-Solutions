def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    l = list()
    for i in keyboards:
        for j in drives:
            if (i+j) <= b:
                l.append(i+j)
    if l == []:
        return -1
    return max(l)