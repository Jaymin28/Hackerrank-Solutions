def utopianTree(n):
    # Write your code here
    h = 1
    if n == 0:
        return 1
    for i in range(1,n+1):
        if i % 2 != 0:
            h *= 2
        else :
            h += 1
    return h