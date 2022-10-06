def minimumDistances(a):
    # Write your code here
    l = list()
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                dist = abs(j-i)
                l.append(dist)
    if l == []:
        return -1
    else :
        return min(l)